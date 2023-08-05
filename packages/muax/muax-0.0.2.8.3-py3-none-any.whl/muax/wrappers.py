"""
    MIT License

    Copyright (c) 2020 Microsoft Corporation.
    Copyright (c) 2021 github.com/coax-dev
    Copyright (c) 2022 bf2504@columbia.edu

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE
"""    

import logging
import os
import re
import datetime
import logging
import time
from collections import deque
from typing import Mapping

import numpy as np
import lz4.frame
import cloudpickle as pickle
import gymnasium
from gymnasium import Wrapper
from gymnasium.spaces import Discrete
from tensorboardX import SummaryWriter

from .utils import action2plane


__all__ = (
    'TrainMonitor',
    'FrameStacking'
)

class LoggerMixin:
    @property
    def logger(self):
        return logging.getLogger(self.__class__.__name__)


def enable_logging(name=None, level=logging.INFO, output_filepath=None, output_level=None):
    r"""
    Enable logging output.
    This executes the following two lines of code:
    .. code:: python
        import logging
        logging.basicConfig(level=logging.INFO)
    Parameters
    ----------
    name : str, optional
        Name of the process that is logging. This can be set to whatever you
        like.
    level : int, optional
        Logging level for the default :py:class:`StreamHandler
        <logging.StreamHandler>`. The default setting is ``level=logging.INFO``
        (which is 20). If you'd like to see more verbose logging messages you
        might set ``level=logging.DEBUG``.
    output_filepath : str, optional
        If provided, a :py:class:`FileHandler <logging.FileHandler>` will be
        added to the root logger via:
        .. code:: python
            file_handler = logging.FileHandler(output_filepath)
            logging.getLogger('').addHandler(file_handler)
    output_level : int, optional
        Logging level for the :py:class:`FileHandler <logging.FileHandler>`. If
        left unspecified, this defaults to ``level``, i.e. the same level as
        the default :py:class:`StreamHandler <logging.StreamHandler>`.
    """
    if name is None:
        fmt = '[%(name)s|%(levelname)s] %(message)s'
    else:
        fmt = f'[{name}|%(name)s|%(levelname)s] %(message)s'
    logging.basicConfig(level=level, format=fmt)
    if output_filepath is not None:
        os.makedirs(os.path.dirname(output_filepath) or '.', exist_ok=True)
        fh = logging.FileHandler(output_filepath)
        fh.setLevel(level if output_level is None else output_level)
        logging.getLogger('').addHandler(fh)


class StreamingSample:
    def __init__(self, maxlen, random_seed=None):
        self._deque = deque(maxlen=maxlen)
        self._count = 0
        self._rnd = np.random.RandomState(random_seed)

    def reset(self):
        self._deque = deque(maxlen=self.maxlen)
        self._count = 0

    def append(self, obj):
        self._count += 1
        if len(self) < self.maxlen:
            self._deque.append(obj)
        elif self._rnd.rand() < self.maxlen / self._count:
            i = self._rnd.randint(self.maxlen)
            self._deque[i] = obj

    @property
    def values(self):
        return list(self._deque)  # shallow copy

    @property
    def maxlen(self):
        return self._deque.maxlen

    def __len__(self):
        return len(self._deque)

    def __bool__(self):
        return bool(self._deque)


class TrainMonitor(Wrapper, LoggerMixin):
    r"""
    Environment wrapper for monitoring the training process.
    This wrapper logs some diagnostics at the end of each episode and it also gives us some handy
    attributes (listed below).
    Parameters
    ----------
    env : gymnasium environment
        A gymnasium environment.
    tensorboard_dir : str, optional
        If provided, TrainMonitor will log all diagnostics to be viewed in tensorboard. To view
        these, point tensorboard to the same dir:
        .. code:: bash
            $ tensorboard --logdir {tensorboard_dir}
    tensorboard_write_all : bool, optional
        You may record your training metrics using the :attr:`record_metrics` method. Setting the
        ``tensorboard_write_all`` specifies whether to pass the metrics on to tensorboard
        immediately (``True``) or to wait and average them across the episode (``False``). The
        default setting (``False``) prevents tensorboard from being fluided by logs.
    log_all_metrics : bool, optional
        Whether to log all metrics. If ``log_all_metrics=False``, only a reduced set of metrics are
        logged.
    smoothing : positive int, optional
        The number of observations for smoothing the metrics. We use the following smooth update
        rule:
        .. math::
            n\ &\leftarrow\ \min(\text{smoothing}, n + 1) \\
            x_\text{avg}\ &\leftarrow\ x_\text{avg}
                + \frac{x_\text{obs} - x_\text{avg}}{n}
    \*\*logger_kwargs
        Keyword arguments to pass on to :func:`coax.utils.enable_logging`.
    Attributes
    ----------
    T : positive int
        Global step counter. This is not reset by ``env.reset()``, use ``env.reset_global()``
        instead.
    ep : positive int
        Global episode counter. This is not reset by ``env.reset()``, use ``env.reset_global()``
        instead.
    t : positive int
        Step counter within an episode.
    G : float
        The return, i.e. amount of reward accumulated from the start of the current episode.
    avg_G : float
        The average return G, averaged over the past 100 episodes.
    dt_ms : float
        The average wall time of a single step, in milliseconds.
    """
    _COUNTER_ATTRS = (
        'T', 'ep', 't', 'G', 'avg_G', '_n_avg_G', '_ep_starttime', '_ep_metrics', '_ep_actions',
        '_tensorboard_dir', '_period')

    def __init__(
            self, env,
            tensorboard_dir=None,
            tensorboard_write_all=False,
            log_all_metrics=False,
            smoothing=10,
            **logger_kwargs):

        super().__init__(env)
        self.log_all_metrics = log_all_metrics
        self.tensorboard_write_all = tensorboard_write_all
        self.smoothing = float(smoothing)
        self.reset_global()
        enable_logging(**logger_kwargs)
        self.logger.setLevel(logger_kwargs.get('level', logging.INFO))
        self._init_tensorboard(tensorboard_dir)

    def reset_global(self):
        r""" Reset the global counters, not just the episodic ones. """
        self.T = 0
        self.ep = 0
        self.t = 0
        self.G = 0.0
        self.avg_G = 0.0
        self._n_avg_G = 0.0
        self._ep_starttime = time.time()
        self._ep_metrics = {}
        self._ep_actions = StreamingSample(maxlen=1000)
        self._period = {'T': {}, 'ep': {}}

    def reset(self, seed=None):
        # write logs from previous episode:
        if self.ep:
            self._write_episode_logs()

        # increment global counters:
        self.T += 1
        self.ep += 1

        # reset episodic counters:
        self.t = 0
        self.G = 0.0
        self._ep_starttime = time.time()
        self._ep_metrics = {}
        self._ep_actions.reset()

        return self.env.reset(seed=seed)

    @property
    def dt_ms(self):
        if self.t <= 0:
            return np.nan
        return 1000 * (time.time() - self._ep_starttime) / self.t

    @property
    def avg_r(self):
        if self.t <= 0:
            return np.nan
        return self.G / self.t

    def step(self, a):
        self._ep_actions.append(a)
        s_next, r, done, truncated, info = self.env.step(a)
        if not info:
            info = {}
        info['monitor'] = {'T': self.T, 'ep': self.ep}
        self.t += 1
        self.T += 1
        self.G += r
        if done or truncated:
            if self._n_avg_G < self.smoothing:
                self._n_avg_G += 1.
            self.avg_G += (self.G - self.avg_G) / self._n_avg_G

        return s_next, r, done, truncated, info

    def record_metrics(self, metrics):
        r"""
        Record metrics during the training process.
        These are used to print more diagnostics.
        Parameters
        ----------
        metrics : dict
            A dict of metrics, of type ``{name <str>: value <float>}``.
        """
        if not isinstance(metrics, Mapping):
            raise TypeError("metrics must be a Mapping")

        # write metrics to tensoboard
        if self.tensorboard is not None and self.tensorboard_write_all:
            for name, metric in metrics.items():
                self.tensorboard.add_scalar(
                    str(name), float(metric), global_step=self.T)

        # compute episode averages
        for k, v in metrics.items():
            if k not in self._ep_metrics:
                self._ep_metrics[k] = v, 1.
            else:
                x, n = self._ep_metrics[k]
                self._ep_metrics[k] = x + v, n + 1

    def get_metrics(self):
        r"""
        Return the current state of the metrics.
        Returns
        -------
        metrics : dict
            A dict of metrics, of type ``{name <str>: value <float>}``.
        """
        return {k: float(x) / n for k, (x, n) in self._ep_metrics.items()}

    def period(self, name, T_period=None, ep_period=None):
        if T_period is not None:
            T_period = int(T_period)
            assert T_period > 0
            if name not in self._period['T']:
                self._period['T'][name] = 1
            if self.T >= self._period['T'][name] * T_period:
                self._period['T'][name] += 1
                return True or self.period(name, None, ep_period)
            return self.period(name, None, ep_period)
        if ep_period is not None:
            ep_period = int(ep_period)
            assert ep_period > 0
            if name not in self._period['ep']:
                self._period['ep'][name] = 1
            if self.ep >= self._period['ep'][name] * ep_period:
                self._period['ep'][name] += 1
                return True
        return False

    @property
    def tensorboard(self):
        if not hasattr(self, '_tensorboard'):
            assert self._tensorboard_dir is not None
            self._tensorboard = SummaryWriter(self._tensorboard_dir)
        return self._tensorboard

    def _init_tensorboard(self, tensorboard_dir):
        if tensorboard_dir is None:
            self._tensorboard_dir = None
            self._tensorboard = None
            return

        # append timestamp to disambiguate instances
        if not re.match(r'.*/\d{8}_\d{6}$', tensorboard_dir):
            tensorboard_dir = os.path.join(
                tensorboard_dir,
                datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))

        # only set/update if necessary
        if tensorboard_dir != getattr(self, '_tensorboard_dir', None):
            self._tensorboard_dir = tensorboard_dir
            if hasattr(self, '_tensorboard'):
                del self._tensorboard

    def _write_episode_logs(self):
        metrics = (
            f'{k:s}: {float(x) / n:.3g}'
            for k, (x, n) in self._ep_metrics.items() if (
                self.log_all_metrics
                or str(k).endswith('/loss')
                or str(k).endswith('/entropy')
                or str(k).endswith('/kl_div')
                or str(k).startswith('throughput/')
            )
        )
        self.logger.info(
            ',\t'.join((
                f'ep: {self.ep:d}',
                f'T: {self.T:,d}',
                f'G: {self.G:.3g}',
                f'avg_r: {self.avg_r:.3g}',
                f'avg_G: {self.avg_G:.3g}',
                f't: {self.t:d}',
                f'dt: {self.dt_ms:.3f}ms',
                *metrics)))

        if self.tensorboard is not None:
            metrics = {
                'episode/episode': self.ep,
                'episode/avg_reward': self.avg_r,
                'episode/return': self.G,
                'episode/steps': self.t,
                'episode/avg_step_duration_ms': self.dt_ms}
            for name, metric in metrics.items():
                self.tensorboard.add_scalar(
                    str(name), float(metric), global_step=self.T)
            if self._ep_actions:
                if isinstance(self.action_space, Discrete):
                    bins = np.arange(self.action_space.n + 1)
                else:
                    bins = 'auto'  # see also: np.histogram_bin_edges.__doc__
                self.tensorboard.add_histogram(
                    tag='actions', values=self._ep_actions.values, global_step=self.T, bins=bins)
            if self._ep_metrics and not self.tensorboard_write_all:
                for k, (x, n) in self._ep_metrics.items():
                    self.tensorboard.add_scalar(str(k), float(x) / n, global_step=self.T)
            self.tensorboard.flush()

    def __getstate__(self):
        state = self.__dict__.copy()   # shallow copy
        if '_tensorboard' in state:
            del state['_tensorboard']  # remove reference to non-pickleable attr
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._init_tensorboard(state['_tensorboard_dir'])

    def get_counters(self):
        r"""
        Get the current state of all internal counters.
        Returns
        -------
        counter : dict
            The dict that contains the counters.
        """
        return {k: getattr(self, k) for k in self._COUNTER_ATTRS}

    def set_counters(self, counters):
        r"""
        Restore the state of all internal counters.
        Parameters
        ----------
        counter : dict
            The dict that contains the counters.
        """
        if not (isinstance(counters, dict) and set(counters) == set(self._COUNTER_ATTRS)):
            raise TypeError(f"invalid counters dict: {counters}")
        self.__setstate__(counters)

    def save_counters(self, filepath):
        r"""
        Store the current state of all internal counters.
        Parameters
        ----------
        filepath : str
            The checkpoint file path.
        """
        counters = self.get_counters()
        os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)

        with lz4.frame.open(filepath, 'wb') as f:
            f.write(pickle.dumps(counters))

    def load_counters(self, filepath):
        r"""
        Restore the state of all internal counters.
        Parameters
        ----------
        filepath : str
            The checkpoint file path.
        """
        with lz4.frame.open(filepath, 'rb') as f:
            counters = pickle.loads(f.read())
        self.set_counters(counters)


class FrameStacking(gymnasium.Wrapper):
    r"""
    Wrapper that does frame stacking (see `DQN paper
    <https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf>`_).
    This implementation is different from the coax's implementation that doesn't perform the
    stacking itself. Instead, it returns a ndarray of frames, which is stacked along the last axis(axis=-1).
    
    Example
    -------
    .. code::
        import gymnasium
        env = gymnasium.make('PongNoFrameskip-v0')
        print(env.observation_space)  # Box(210, 160, 3)
        env = FrameStacking(env, num_frames=2)
        print(env.observation_space)  # Tuple((Box(210, 160, 3), Box(210, 160, 3)))
    Parameters
    ----------
    env : gymnasium-style environment
        The original environment to be wrapped.
    num_frames : positive int
        Number of frames to stack.
    new_axis: bool
        To stack on the new axis or on the last axis. Default is True, that is, creates a new axis.
    """
    def __init__(self, env, num_frames, new_axis: bool = True):
        if not (isinstance(num_frames, int) and num_frames > 0):
            raise TypeError(f"num_frames must be a positive int, got: {num_frames}")

        super().__init__(env)
        self.new_axis = new_axis
        self.observation_space = self._new_observation_space(env, num_frames)
        self._frames = deque(maxlen=num_frames)

    def step(self, action):
        observation, reward, done, truncated, info = self.env.step(action)
        self._frames.append(observation)
        if self.new_axis:
          observation_stacked = np.stack(self._frames, axis=-1)
        else:
          observation_stacked = np.concatenate(self._frames, axis=-1)
        return observation_stacked, reward, done, truncated, info

    def reset(self, **kwargs):
        observation, info = self.env.reset(**kwargs)
        self._frames.extend(observation for _ in range(self._frames.maxlen))
        if self.new_axis:
          observation_stacked = np.stack(self._frames, axis=-1)
        else:
          observation_stacked = np.concatenate(self._frames, axis=-1)
        return observation_stacked, info  # shallow copy
    
    def _new_observation_space(self, env, num_frames):
        mutable_ = list(env.observation_space.shape)
        if self.new_axis:
          mutable_.append(num_frames)
          new_low = np.stack([env.observation_space.low for _ in range(num_frames)], axis=-1)
          new_high = np.stack([env.observation_space.high for _ in range(num_frames)], axis=-1)
        else:
          mutable_[-1] = mutable_[-1] * num_frames
          new_low = np.concatenate([env.observation_space.low for _ in range(num_frames)], axis=-1)
          new_high = np.concatenate([env.observation_space.high for _ in range(num_frames)], axis=-1)
        new_shape = tuple(mutable_)
        new_obs_space = type(env.observation_space)(shape=new_shape, low=new_low, high=new_high, dtype=env.observation_space.dtype)
        return new_obs_space


class ActionHistory(gymnasium.Wrapper):
    r"""
    Wrapper that integrated action history in observation (see `MuZero paper
    <https://www.nature.com/articles/s41586-020-03051-4>`_).
    This implementation expects observation without batch dimension, and processes the action differently based on
    the observation's shape. If observation is 1D (len(obs.shape)==1), the action will be encoded into one hot and 
    appended to the observation. If observation is not 1D (len(obs.shape) > 1), for instance, (H, W, C), then the action
    will be encoded as plane, that has the shape (H, W, 1), and concatenated along the last axis(By default).
    For `reset()`, an additional action that represents "do nothing" is encoded and appended to the observation. As for 
    one hot, this means there will be (num_actions + 1) new dimensions, with the last dimension be the "do nothing" action.
    As for plane, a plane of num_actions represents "do nothing". Normalization is applied if `scale_action` is True.
    That is, the action dimension will `/= num_actions`
    
    Example
    -------
    .. code::
        import gymnasium
        env = gymnasium.make('PongNoFrameskip-v0')
        print(env.observation_space)  # Box(210, 160, 3)
        env = ActionHistory(env, num_frames=2)
        print(env.observation_space)  # Box(210, 160, 4)
    Parameters
    ----------
    env : gymnasium-style environment
        The original environment to be wrapped.
    
    num_actions: int
        The maximum number of actions in the env.

    axis : int
        The axis to concatenate the action.

    scale_action: bool
        Whether to scale the action dimension to [0, 1] range. Default is True.
    """
    def __init__(self, env, num_actions: int, axis: int = -1, scale_action: bool = True):
        super().__init__(env)
        self.axis = axis 
        self.num_actions = num_actions
        self.scale_action = scale_action
        self.observation_space, self._additional_axis = self._new_observation_space(env, num_actions, axis)

    def step(self, action):
        observation, reward, done, truncated, info = self.env.step(action)
        observation_action = self._append_action(observation, action)
        return observation_action, reward, done, truncated, info

    def reset(self, **kwargs):
        observation, info = self.env.reset(**kwargs)
        observation_action = self._append_action(observation, self.num_actions)
        return observation_action, info  
    
    def _append_action(self, obs, a):
        num_actions = self.num_actions
        if len(obs.shape) > 1:
            a_broadcast = action2plane(a, self._additional_axis)
            if self.scale_action:
              a_broadcast /= num_actions
            obs_a = np.concatenate([obs, a_broadcast], axis=self.axis)
        else:
            a_onehot = np.zeros((num_actions + 1,))
            a_onehot[a] = 1
            obs_a = np.concatenate([obs, a_onehot], axis=self.axis)
        return obs_a 
    
    def _new_observation_space(self, env, num_actions, axis):
        if len(env.observation_space.shape) > 1:
            mutable_ = list(env.observation_space.shape)
            mutable_[axis] += 1
            new_shape = tuple(mutable_)
            additional_axis_ = list(env.observation_space.shape)
            additional_axis_[axis] = 1
            additional_axis = tuple(additional_axis_)
            new_low = np.concatenate([env.observation_space.low, action2plane(0, additional_axis)], axis=axis)
            if not self.scale_action:
              new_high = np.concatenate([env.observation_space.high, action2plane(num_actions, additional_axis)], axis=axis)
            else:
              new_high = np.concatenate([env.observation_space.high, action2plane(1, additional_axis)], axis=axis)
        else:
            mutable_ = list(env.observation_space.shape)
            mutable_[axis] += num_actions + 1
            new_shape = tuple(mutable_)
            additional_axis_ = list(env.observation_space.shape)
            additional_axis_[axis] = num_actions + 1
            additional_axis = tuple(additional_axis_)
            new_low = np.concatenate([env.observation_space.low, action2plane(0, additional_axis)], axis=axis)
            new_high = np.concatenate([env.observation_space.high, action2plane(1, additional_axis)], axis=axis)
        
        self._additional_axis = additional_axis
        new_obs_space = type(env.observation_space)(shape=new_shape, low=new_low, high=new_high, dtype=env.observation_space.dtype)
        return new_obs_space, additional_axis
