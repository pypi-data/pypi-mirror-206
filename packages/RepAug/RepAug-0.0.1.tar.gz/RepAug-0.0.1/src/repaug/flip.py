from torch import Tensor
import torchvision.transforms.functional as TF
import numpy as np

from .utils import _check_type, _convert_type, accepted_types


class RandomHorizontalFlip(object):
    def __init__(self, p: float = 0.5, seed: int = 42) -> None:
        super().__init__()
        assert isinstance(p, float) and 0. <= p <= 1., f"`p` should be a float in the range [0, 1]. Found `p` = {p}."
        self.p = p
        self.rng = np.random.default_rng(seed)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        img = TF.hflip(img) if self.rng.random() <= self.p else img

        return _convert_type(img, orig_type)


class RandomVerticalFlip(object):
    def __init__(self, p: float = 0.5, seed: int = 42) -> None:
        super().__init__()
        assert isinstance(p, float) and 0. <= p <= 1., f"`p` should be a float in the range [0, 1]. Found `p` = {p}."
        self.p = p
        self.rng = np.random.default_rng(seed)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        img = TF.vflip(img) if self.rng.random() <= self.p else img

        return _convert_type(img, orig_type)
