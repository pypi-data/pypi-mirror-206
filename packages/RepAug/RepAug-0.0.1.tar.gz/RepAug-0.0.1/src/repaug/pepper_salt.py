import torch
from torch import Tensor
import numpy as np

from typing import Union
from .utils import _check_type, _convert_type, accepted_types


class Pepper(object):
    def __init__(
        self,
        num_peppers: Union[int, float] = 100,
        max_spiciness: float = 0.01,
        seed: int = 42
    ) -> None:
        super().__init__()
        assert isinstance(num_peppers, (int, float)) and num_peppers >= 0
        self.num_peppers = num_peppers
        assert isinstance(max_spiciness, float) and 0. <= max_spiciness <= 1.
        self.max_spiciness = max_spiciness
        self.rng = np.random.default_rng(seed)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        h, w = img.shape[-2:]
        num_peppers = self.num_peppers if isinstance(self.num_peppers, int) else int(self.num_peppers * h * w)
        idx_h = self.rng.choice(a=h, size=num_peppers)
        idx_w = self.rng.choice(a=w, size=num_peppers)

        peppers = torch.from_numpy(self.rng.random((*img.shape[:-2], num_peppers), dtype=np.float32) * self.max_spiciness)
        img[..., idx_h, idx_w] = peppers  # sprinkle peppers.

        return _convert_type(img, orig_type)


class Salt(object):
    def __init__(
        self,
        num_salts: Union[int, float] = 100,
        max_saltiness: float = 0.01,
        seed: int = 42
    ) -> None:
        super().__init__()
        assert isinstance(num_salts, (int, float)) and num_salts >= 0
        self.num_salts = num_salts
        assert isinstance(max_saltiness, float) and 0. <= max_saltiness <= 1.
        self.max_saltiness = max_saltiness
        self.rng = np.random.default_rng(seed)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        h, w = img.shape[-2:]
        num_salts = self.num_salts if isinstance(self.num_salts, int) else int(self.num_salts * h * w)
        idx_h = self.rng.choice(a=h, size=num_salts)
        idx_w = self.rng.choice(a=w, size=num_salts)

        salts = torch.from_numpy(1. - (self.rng.random((*img.shape[:-2], num_salts), dtype=np.float32) * self.max_saltiness))
        img[..., idx_h, idx_w] = salts  # sprinkle salts.

        return _convert_type(img, orig_type)
