import random
import os
import numpy as np
import torch

from pathlib import Path


def normalize_decoupled(data, cols):
    data[cols] = (data[cols] - data[cols].mean()) / data[cols].std()


def normalize_coupled(data, cols):
    centered = data[cols] - data[cols].mean()
    distdev = (centered ** 2).sum(axis=1).mean() ** 0.5
    data[cols] = centered / distdev


# see https://gist.github.com/ihoromi4/b681a9088f348942b01711f251e5f964
def apply_global_seed(seed: int):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)

    np.random.seed(seed)

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = True


def count_trainable_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def is_model_on_gpu(model):
    return next(model.parameters()).is_cuda


def resolve_path(*paths):
    return str(Path(__file__).parent.joinpath(*paths).absolute())
