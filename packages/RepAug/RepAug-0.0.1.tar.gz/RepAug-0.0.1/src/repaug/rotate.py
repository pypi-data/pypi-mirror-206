from torch import Tensor
import torchvision.transforms.functional as TF
import numpy as np
from typing import Union, Sequence

from .utils import _check_type, _convert_type, accepted_types


class RandomRotation(object):
    def __init__(self, degrees: Union[int, Sequence] = (-30, 30), seed: int = 42) -> None:
        super().__init__()
        degrees = (-degrees, degrees) if isinstance(degrees, int) else degrees
        assert len(degrees) == 2 and -360 <= degrees[0] <= degrees[1] <= 360, f"Expected `degrees` to be an int or a sequence (min, max) ⊆ [-360, 360] of length 2. Found {degrees}."
        self.degrees = degrees
        self.rng = np.random.default_rng(seed)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        angle = self.rng.uniform(*self.degrees)
        img = TF.rotate(img, angle)

        return _convert_type(img, orig_type)


class Random90Rotation(object):
    def __init__(self, seed: int = 42) -> None:
        super().__init__()
        self.rng = np.random.default_rng(seed)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        angle = int(self.rng.choice([0, 90, 180, 270]))
        img = TF.rotate(img, angle)

        return _convert_type(img, orig_type)


class Random180Rotation(object):
    def __init__(self, seed: int = 42) -> None:
        super().__init__()
        self.rng = np.random.default_rng(seed)
    
    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        img = TF.rotate(img, 180) if self.rng.choice([True, False]) else img

        return _convert_type(img, orig_type)
