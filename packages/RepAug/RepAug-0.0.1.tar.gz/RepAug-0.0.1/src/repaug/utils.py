import torch
from torch import Tensor
from torchvision.transforms import InterpolationMode
import torchvision.transforms.functional as TF

import numpy as np
from PIL import Image

from typing import Union, Sequence, Optional, Tuple


accepted_types = (Image.Image, Tensor)

def _check_type(img: accepted_types) -> None:
    assert isinstance(img, accepted_types), f"Expected `img` to be of type PIL.Image or torch.Tensor. Found {type(img)}."

def _convert_type(img: accepted_types, target_type) -> accepted_types:
    assert target_type in accepted_types, f"Expected `target_type` to be one of {accepted_types}. Found {target_type}."

    if target_type == Tensor:
        if isinstance(img, Image.Image):
            img = TF.to_tensor(img)

        assert isinstance(img, Tensor)

    elif target_type == Image.Image:
        if isinstance(img, Tensor):
            img = TF.to_pil_image(img)

        assert isinstance(img, Image.Image)

    return img













