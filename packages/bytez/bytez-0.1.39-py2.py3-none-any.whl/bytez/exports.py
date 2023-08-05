from dataclasses import dataclass
from bytez.tasks.super_resolution import SuperResolutionModels
from bytez.tasks.style_transfer import StyleTransferModels
from bytez.task_list import task_list
import re


def concat_non_alphanumeric(arr):
    updated_arr = []
    for item in arr:
        updated_item = re.sub(r'\W+', '_', item)
        updated_arr.append(updated_item)
    return updated_arr

# TODO make this dynamically import from the tasks modules


# Define base class for dynamically generated attributes
@dataclass
class Task:
    pass


for task_name in concat_non_alphanumeric(task_list):
    setattr(Task, task_name, None)


@dataclass
class model:
    holmes_alan_dsrvae = SuperResolutionModels.holmes_alan_dsrvae
    cmd_style_transfer = StyleTransferModels.cmd_style_transfer
    fast_style_transfer = StyleTransferModels.fast_style_transfer
    tensorflow_fast_style = StyleTransferModels.tensorflow_fast_style


@dataclass
class task(Task):
    super_resolution = SuperResolutionModels
    style_transfer = StyleTransferModels
