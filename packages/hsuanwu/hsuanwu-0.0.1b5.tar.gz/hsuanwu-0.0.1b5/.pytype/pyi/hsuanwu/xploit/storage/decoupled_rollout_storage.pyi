# (generated with --quick)

import gymnasium as gym
import hsuanwu.xploit.storage.base
import torch as th
from typing import Any, Type

BaseStorage: Type[hsuanwu.xploit.storage.base.BaseStorage]
BatchSampler: Any
DictConfig: Any
SubsetRandomSampler: Any

class DecoupledRolloutStorage(hsuanwu.xploit.storage.base.BaseStorage):
    __doc__: str
    _action_dim: Any
    _discount: float
    _gae_lambda: float
    _global_step: int
    _num_envs: int
    _num_steps: int
    actions: Any
    adv_preds: Any
    advantages: Any
    log_probs: Any
    obs: Any
    returns: Any
    rewards: Any
    terminateds: Any
    truncateds: Any
    values: Any
    def __init__(self, observation_space, action_space, device: str = ..., num_steps: int = ..., num_envs: int = ..., discount: float = ..., gae_lambda: float = ...) -> None: ...
    def add(self, obs, actions, rewards, terminateds, truncateds, next_obs, log_probs, values, adv_preds) -> None: ...
    def compute_returns_and_advantages(self, last_values) -> None: ...
    def sample(self, num_mini_batch: int = ...) -> generator: ...
    def update(self) -> None: ...
