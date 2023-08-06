# (generated with --quick)

import gymnasium as gym
import hsuanwu.xploit.agent.base
import hsuanwu.xploit.agent.network
import os
import pathlib
import torch as th
from hsuanwu.xploit.agent import utils
from torch.nn import functional as F
from typing import Any, Dict, List, Optional, Tuple, Type, Union

BaseAgent: Type[hsuanwu.xploit.agent.base.BaseAgent]
DEFAULT_CFGS: Dict[str, Union[int, str, Dict[str, Optional[Union[float, int, str, Dict[nothing, nothing], Type[Union[int, str]]]]]]]
DictConfig: Any
MATCH_KEYS: Dict[str, Union[str, List[str]]]
OffPolicyDeterministicActor: Type[hsuanwu.xploit.agent.network.OffPolicyDeterministicActor]
OffPolicyDoubleCritic: Type[hsuanwu.xploit.agent.network.OffPolicyDoubleCritic]
Path: Type[pathlib.Path]

class DrQv2(hsuanwu.xploit.agent.base.BaseAgent):
    __doc__: str
    actor: Any
    actor_opt: Any
    aug: Any
    critic: Any
    critic_opt: Any
    critic_target: Any
    critic_target_tau: float
    dist: Any
    encoder: Any
    encoder_opt: Any
    irs: Any
    training: bool
    update_every_steps: int
    def __init__(self, observation_space, action_space, device: str, feature_dim: int, lr: float, eps: float, hidden_dim: int, critic_target_tau: float, update_every_steps: int) -> None: ...
    def act(self, obs, training: bool = ..., step: int = ...) -> Tuple[Any]: ...
    def integrate(self, **kwargs) -> None: ...
    def load(self, path: str) -> None: ...
    def save(self, path: pathlib.Path) -> None: ...
    def train(self, training: bool = ...) -> None: ...
    def update(self, replay_storage, step: int = ...) -> Dict[str, float]: ...
    def update_actor(self, obs, step: int) -> Dict[str, float]: ...
    def update_critic(self, obs, action, reward, discount, next_obs, step: int) -> Dict[str, float]: ...
