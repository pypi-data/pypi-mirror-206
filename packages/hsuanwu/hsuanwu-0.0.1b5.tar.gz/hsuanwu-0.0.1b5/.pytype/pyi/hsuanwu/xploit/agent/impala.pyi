# (generated with --quick)

import gymnasium as gym
import hsuanwu.xploit.agent.base
import hsuanwu.xploit.agent.network
import omegaconf
import os
import pathlib
import threading
import torch as th
from torch import nn
from torch.nn import functional as F
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

BaseAgent: Type[hsuanwu.xploit.agent.base.BaseAgent]
DEFAULT_CFGS: Dict[str, Union[int, str, Dict[str, Optional[Union[float, int, str, Dict[nothing, nothing], Type[Union[int, str]]]]]]]
DictConfig: Any
DistributedActorCritic: Type[hsuanwu.xploit.agent.network.DistributedActorCritic]
MATCH_KEYS: Dict[str, Union[str, List[str]]]
Path: Type[pathlib.Path]

_T = TypeVar('_T')

class IMPALA(hsuanwu.xploit.agent.base.BaseAgent):
    __doc__: str
    actor: hsuanwu.xploit.agent.network.DistributedActorCritic
    baseline_coef: float
    discount: float
    dist: Any
    ent_coef: float
    learner: hsuanwu.xploit.agent.network.DistributedActorCritic
    lr_scheduler: Any
    max_grad_norm: float
    opt: Any
    training: bool
    def __init__(self, observation_space, action_space, device: str, feature_dim: int, lr: float, eps: float, use_lstm: bool, ent_coef: float, baseline_coef: float, max_grad_norm: float, discount: float) -> None: ...
    def act(self, *kwargs) -> None: ...
    def integrate(self, **kwargs) -> None: ...
    def load(self, path: str) -> None: ...
    def save(self, path: pathlib.Path) -> None: ...
    def train(self, training: bool = ...) -> None: ...
    @staticmethod
    def update(cfgs, actor_model, learner_model, batch: dict, init_actor_states: tuple, optimizer, lr_scheduler, lock = ...) -> Dict[str, tuple]: ...

class VTraceLoss:
    clip_pg_rho_threshold: Any
    clip_rho_threshold: Any
    dist: None
    def __call__(self, batch) -> Tuple[Any, Any, Any]: ...
    def __init__(self, clip_rho_threshold = ..., clip_pg_rho_threshold = ...) -> None: ...
    def compute_ISW(self, target_dist, behavior_dist, action) -> Any: ...

def deepcopy(x: _T, memo: Optional[Dict[int, Any]] = ..., _nil = ...) -> _T: ...
