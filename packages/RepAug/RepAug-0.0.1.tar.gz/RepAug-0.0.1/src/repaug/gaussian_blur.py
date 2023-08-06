from torch import Tensor
import torchvision.transforms.functional as TF
import numpy as np
from typing import Union, Sequence, Optional

from .utils import _check_type, _convert_type, accepted_types


class RandomGaussianBlur(object):
    def __init__(
        self,
        kernel_size: Union[int, Sequence] = (3, 5, 7, 9),
        sigma: Optional[Union[float, Sequence]] = None,
        seed: int = 42
    ) -> None:
        super().__init__()
        kernel_size = [kernel_size] if isinstance(kernel_size, int) else kernel_size
        sigma = (sigma, sigma) if isinstance(sigma, float) else sigma
        assert isinstance(kernel_size, Sequence) and all(kernel_size_ % 2 == 1 for kernel_size_ in kernel_size), f"Expected `kernel_size` to be an odd integer or a sequence of odd integers. Found {kernel_size}."
        assert sigma is None or (len(sigma) == 2 and 0. <= sigma[0] <= sigma[1]), f"Expected `sigma` to be a float or a sequence (min, max) ⊆ [0., ∞) of length 2 or None. Found {sigma}."
        self.kernel_size = kernel_size
        self.sigma = sigma
        self.rng = np.random.default_rng(seed)

    def __call__(self, img: accepted_types) -> accepted_types:
        _check_type(img)
        orig_type = type(img)
        img = _convert_type(img, Tensor)

        kernel_size = int(self.rng.choice(self.kernel_size))
        sigma = float(self.rng.uniform(self.sigma[0], self.sigma[1])) if self.sigma is not None else self.sigma
        img = TF.gaussian_blur(img, kernel_size, sigma)

        return _convert_type(img, orig_type)
