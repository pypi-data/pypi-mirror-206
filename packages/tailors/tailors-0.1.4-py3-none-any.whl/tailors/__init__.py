# -*- coding: utf-8 -*-
__version__ = '0.1.4'

import os
import random
from collections import UserDict
from typing import List

import hao
import torch
from decorator import decorator
from torch.nn import functional as F

LOGGER = hao.logs.get_logger(__name__)


def freeze(model):
    for param in model.parameters():
        param.requires_grad = False


def unfreeze(model):
    for param in model.parameters():
        param.requires_grad = True


def init(model):
    for layer in model.modules():
        if isinstance(layer, torch.nn.Conv2d):
            torch.nn.init.kaiming_normal_(layer.weight, mode='fan_out', nonlinearity='relu')
            if layer.bias is not None:
                torch.nn.init.constant_(layer.bias, val=0.0)

        elif isinstance(layer, torch.nn.BatchNorm2d):
            torch.nn.init.constant_(layer.weight, val=1.0)
            torch.nn.init.constant_(layer.bias, val=0.0)

        elif isinstance(layer, torch.nn.Linear):
            torch.nn.init.xavier_normal_(layer.weight)
            if layer.bias is not None:
                torch.nn.init.constant_(layer.bias, val=0.0)


def set_seed(seed, deterministic=True, benchmark=False):
    if seed is None:
        seed = random.randint(0, 10000)
        LOGGER.info(f"[seed] using random generated seed: {seed}")
    else:
        LOGGER.info(f"[seed] using random seed: {seed}")

    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    try:
        import numpy as np
        np.random.seed(seed)
    except ImportError:
        pass
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = deterministic
    torch.backends.cudnn.benchmark = benchmark


def move_to_device(data, device, non_blocking=True):
    if device is None:
        return
    if isinstance(data, (dict, UserDict)):
        return {k: move_to_device(v, device, non_blocking) for k, v in data.items()}
    elif isinstance(data, tuple):
        if hasattr(data, '_asdict') and hasattr(data, '_fields'):
            cls = type(data)
            return cls(*[move_to_device(v, device, non_blocking) for v in data])
        else:
            return tuple([move_to_device(v, device, non_blocking) for v in data])
    elif isinstance(data, list):
        return [move_to_device(v, device, non_blocking) for v in data]
    elif isinstance(data, torch.Tensor):
        return data.to(device, non_blocking=non_blocking)
    return data


@decorator
def auto_device(func, *a, **kw):
    def wrapper(self, *args, **kwargs):
        args = move_to_device(args, self.device)
        kwargs = move_to_device(kwargs, self.device)
        return func(self, *args, **kwargs)
    return wrapper(*a, **kw)


def off_tensor(data):
    if data is None:
        return None
    if isinstance(data, dict):
        return {k: off_tensor(v) for k, v in data.items()}
    elif isinstance(data, tuple):
        return tuple([off_tensor(v) for v in data])
    elif isinstance(data, list):
        return [off_tensor(v) for v in data]
    elif isinstance(data, torch.Tensor):
        return data.detach().cpu() if data.is_sparse else data.tolist()
    return data


def append_batch(items, batch):
    batch = off_tensor(batch)
    if isinstance(batch, tuple):
        hao.lists.add_tuple_to_list(items, batch)
    elif isinstance(batch, torch.Tensor):
        items.append(batch)
    else:
        items.extend(batch)


def multi_hot(items: List[int], n_classes: int, dtype=torch.float32):
    data = torch.LongTensor(items)
    onehot = F.one_hot(data, num_classes=n_classes)
    return onehot.sum(dim=0).to(dtype)
