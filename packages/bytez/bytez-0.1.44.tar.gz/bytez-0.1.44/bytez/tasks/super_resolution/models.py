from bytez.tasks.super_resolution._models.holmes_alan_dsrvae import HolmesAlanDsrvaeModel
from dataclasses import dataclass


@dataclass
class SuperResolutionModels:
    pass
    holmes_alan_dsrvae = HolmesAlanDsrvaeModel().inference