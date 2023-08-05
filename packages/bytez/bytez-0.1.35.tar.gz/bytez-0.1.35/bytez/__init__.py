from dataclasses import dataclass
from bytez.tasks.super_resolution import SuperResolutionModels
from bytez.tasks.style_transfer import StyleTransferModels
from bytez.task_list import task_list

# Define base class for dynamically generated attributes


@dataclass
class Task:
    pass


for task_name in task_list:
    setattr(Task, task_name, None)

# Create tasks class with dynamically generated and predefined attributes


@dataclass
class tasks(Task):
    super_resolution: SuperResolutionModels
    style_transfer: StyleTransferModels

# Create models class with predefined attributes


@dataclass
class models:
    holmes_alan_dsrvae = SuperResolutionModels.holmes_alan_dsrvae
    cmd_style_transfer = StyleTransferModels.cmd_style_transfer
    fast_style_transfer = StyleTransferModels.fast_style_transfer
    tensorflow_fast_style = StyleTransferModels.tensorflow_fast_style


__all__ = ['models', 'tasks']
