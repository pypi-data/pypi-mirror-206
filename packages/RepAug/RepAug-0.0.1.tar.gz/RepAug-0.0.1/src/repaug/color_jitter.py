from torch import Tensor
import torchvision.transforms.functional as TF
import numpy as np
from typing import Union, Sequence

from .utils import _check_type, _convert_type, accepted_types


class RandomColorJitter(object):
    def __init__(
        self,
        brightness: Union[float, Sequence] = 0.2,
        contrast: Union[float, Sequence] = 0.2,
        saturation: Union[float, Sequence] = 0.2,
        hue: Union[float, Sequence] = 0.1,
        seed: int = 42
    ) -> None:
        super().__init__()
        brightness = (max(0., 1. - brightness), 1. + brightness) if isinstance(brightness, float) else brightness
        contrast = (max(0., 1. - contrast), 1. + contrast) if isinstance(contrast, float) else contrast
        saturation = (max(0., 1. - saturation), 1. + saturation) if isinstance(saturation, float) else saturation
        hue = (-hue, hue) if isinstance(hue, float) else hue
        assert len(brightness) == 2 and 0. <= brightness[0] <= brightness[1] <= 2., f"Expected `brightness` to be a float ∈ [0., 1.] or a sequence (min, max) ⊆ [0., 2.] of length 2. Found {brightness}."
        assert len(contrast) == 2 and 0. <= contrast[0] <= contrast[1] <= 2., f"Expected `contrast` to be a float ∈ [0., 1.] or a sequence (min, max) ⊆ [0., 2.] of length 2. Found {contrast}."
        assert len(saturation) == 2 and 0. <= saturation[0] <= saturation[1] <= 2., f"Expected `saturation` to be a float ∈ [0., 1.] or a sequence (min, max) ⊆ [0., 2.] of length 2. Found {saturation}."
        assert len(hue) == 2 and -0.5 <= hue[0] <= hue[1] <= 0.5, f"Expected `hue` to be a float ∈ [0., 0.5] or a sequence (min, max) ⊆ [-0.5, 0.5] of length 2. Found {hue}."

        self.brightness = brightness
        self.contrast = contrast
        self.saturation = saturation
        self.hue = hue
        self.rng = np.random.default_rng(seed)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        brightness = self.rng.uniform(self.brightness[0], self.brightness[1])
        contrast = self.rng.uniform(self.contrast[0], self.contrast[1])
        saturation = self.rng.uniform(self.saturation[0], self.saturation[1])
        hue = self.rng.uniform(self.hue[0], self.hue[1])

        img = TF.adjust_brightness(img, brightness)
        img = TF.adjust_contrast(img, contrast)
        img = TF.adjust_saturation(img, saturation)
        img = TF.adjust_hue(img, hue)

        return _convert_type(img, orig_type)
