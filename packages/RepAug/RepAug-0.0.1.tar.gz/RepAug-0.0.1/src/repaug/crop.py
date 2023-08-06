from torch import Tensor
from torchvision.transforms import InterpolationMode
import torchvision.transforms.functional as TF
import numpy as np
from typing import Union, Sequence, Tuple, Optional

from .utils import _check_type, _convert_type, accepted_types


class RandomCrop(object):
    def __init__(
        self,
        size: Union[int, Sequence] = 112,
        scale: Optional[Union[float, Sequence]] = None,
        seed: int = 42
    ) -> None:
        super().__init__()
        size = (size, size) if isinstance(size, int) else size
        scale = (scale, scale) if isinstance(scale, float) else scale

        if size is not None:
            assert scale is None, f"Expected `scale` to be None when `size` is specified. Found {scale}."
            assert len(size) == 2 and 1. <= size[0] <= size[1], f"Expected `size` to be a float ∈ [1., ∞) or a sequence (min, max) ⊆ [1., ∞) of length 2. Found {size}."

        if scale is not None:
            assert size is None, f"Expected `size` to be None when `scale` is specified. Found {size}."
            assert len(scale) == 2 and 0. <= scale[0] <= scale[1] <= 1., f"Expected `scale` to be a float ∈ [0., 1.] or a sequence (min, max) ⊆ [0., 1.] of length 2. Found {scale}."

        self.size = size
        self.scale = scale
        self.corners = ["tl", "tr", "bl", "br"]
        self.rng = np.random.default_rng(seed)

    def __generate_crop_size__(self, h: int, w: int) -> Tuple[int, int]:
        if self.size is not None:
            crop_h, crop_w = self.size[0] + self.rng.random() * (self.size[1] - self.size[0]), self.size[0] + self.rng.random() * (self.size[1] - self.size[0])
            crop_h, crop_w = int(min(crop_h, h)), int(min(crop_w, w))
        else:
            scale_h, scale_w = self.scale[0] + self.rng.random() * (self.scale[1] - self.scale[0]), self.scale[0] + self.rng.random() * (self.scale[1] - self.scale[0])
            crop_h, crop_w = int(h * scale_h), int(w * scale_w)
        return (crop_h, crop_w)

    def __random_crop__(self, img: Tensor) -> Tensor:
        h, w = img.shape[-2:]
        crop_h, crop_w = self.__generate_crop_size__(h, w)

        top = self.rng.choice(h - crop_h)
        left = self.rng.choice(w - crop_w)

        return TF.crop(img, top=top, left=left, height=crop_h, width=crop_w)

    def __corner_crop__(self, corner: str, img: Tensor) -> Tensor:
        assert corner in self.corners
        h, w = img.shape[-2:]
        crop_h, crop_w = self.__generate_crop_size__(h, w)

        if corner == "tl":
            top, left = 0, 0
        elif corner == "tr":
            top, left = 0, w - crop_w
        elif corner == "bl":
            top, left = h - crop_h, 0
        else:
            top, left = h - crop_h, w - crop_w

        return TF.crop(img, top=top, left=left, height=crop_h, width=crop_w)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        p = self.rng.random()
        if 0 <= p < 0.8:
            img = self.__random_crop__(img)
        elif 0.8 <= p < 0.85:
            img = self.__corner_crop__(self.corners[0], img)
        elif 0.85 <= p < 0.9:
            img = self.__corner_crop__(self.corners[1], img)
        elif 0.9 <= p < 0.95:
            img = self.__corner_crop__(self.corners[2], img)
        else:
            img = self.__corner_crop__(self.corners[3], img)

        return _convert_type(img, orig_type)


class RandomResizedCrop(RandomCrop):
    def __init__(self, scale: Union[float, Sequence] = (0.75, 1.0), seed: int = 42) -> None:
        super(RandomResizedCrop, self).__init__(size=None, scale=scale, seed=seed)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)
        h, w = img.shape[-2:]

        img = super().__call__(img)
        img = TF.resize(img, size=(h, w), interpolation=InterpolationMode.BILINEAR, antialias=True)
        return _convert_type(img, orig_type)
