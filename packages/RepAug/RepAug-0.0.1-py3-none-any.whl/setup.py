from setuptools import setup
from setuptools import find_packages


VERSION = "0.0.1"

setup(
    name="pip ",
    version=VERSION,
    description="A package for augmenting vision data in a reproducible way.",
    packages=find_packages(),
    zip_safe=False,
)
