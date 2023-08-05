import torch
import gc

from .const import SD15_MODELS
from .helper import switch_mps_device
from .model.controlnet import ControlNet
# from model.fcf import FcF
# from model.lama import LaMa
from .model.ldm import LDM
# from model.manga import Manga
# from model.mat import MAT
# from model.paint_by_example import PaintByExample
# from model.instruct_pix2pix import InstructPix2Pix
from .model.sd import SD15, SD2, Anything4, RealisticVision14
# from model.zits import ZITS
# from model.opencv2 import OpenCV2
from .schema import Config

models = {
    # "lama": LaMa,
    "ldm": LDM,
    # "zits": ZITS,
    # "mat": MAT,
    # "fcf": FcF,
    SD15.name: SD15,
    Anything4.name: Anything4,
    RealisticVision14.name: RealisticVision14,
    # "cv2": OpenCV2,
    # "manga": Manga,
    "sd2": SD2,
    # "paint_by_example": PaintByExample,
    # "instruct_pix2pix": InstructPix2Pix,
}


class ModelManager:
    def __init__(self, name: str, device: torch.device, **kwargs):
        # print(name)
        self.name = name
        self.device = device
        self.kwargs = kwargs
        self.model = self.init_model(name, device, **kwargs)

    def init_model(self, name: str, device, **kwargs):
        # print(name)
        if name in SD15_MODELS and kwargs.get("sd_controlnet", True):
            # print("yes")
            return ControlNet(device, **{**kwargs, "name": name})

        if name in models:
            model = models[name](device, **kwargs)
        else:
            raise NotImplementedError(f"Not supported model: {name}")
        return model

    def is_downloaded(self, name: str) -> bool:
        if name in models:
            return models[name].is_downloaded()
        else:
            raise NotImplementedError(f"Not supported model: {name}")

    def __call__(self, image, mask, config: Config):
        return self.model(image, mask, config)

    def switch(self, new_name: str):
        if new_name == self.name:
            return
        try:
            if torch.cuda.memory_allocated() > 0:
                # Clear current loaded model from memory
                torch.cuda.empty_cache()
                del self.model
                gc.collect()

            self.model = self.init_model(
                new_name, switch_mps_device(new_name, self.device), **self.kwargs
            )
            self.name = new_name
        except NotImplementedError as e:
            raise e
