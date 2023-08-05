from dataclasses import dataclass
from bytez.tasks.super_resolution import SuperResolutionModels
from bytez.tasks.style_transfer import StyleTransferModels
from bytez.task_list import task_list

# TODO make this dynamically import from the tasks modules


@dataclass
class model:
    holmes_alan_dsrvae = SuperResolutionModels.holmes_alan_dsrvae
    cmd_style_transfer = StyleTransferModels.cmd_style_transfer
    fast_style_transfer = StyleTransferModels.fast_style_transfer
    tensorflow_fast_style = StyleTransferModels.tensorflow_fast_style


@dataclass
class task:
    for task_name in task_list:
        setattr(task_name, task_name, None)
    super_resolution = SuperResolutionModels
    style_transfer = StyleTransferModels


__all__ = ['model, task']
