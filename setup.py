import os
import functools
from setuptools import setup, find_packages

_IN_PACKAGE_DIR = functools.partial(os.path.join, "pyformance")

with open(_IN_PACKAGE_DIR("__version__.py")) as version_file:
    exec(version_file.read())

setup(
    name="pyformance",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
    ],
    description="Performance metrics, based on Coda Hale's Yammer metrics",
    license="Apache 2.0",
    author="Omer Getrel",
    author_email="omer.gertel@gmail.com",
    version=__version__,
    packages=find_packages(),
    data_files=[],
    scripts=[],
    python_requires=">=3.12",  # also update classifiers
)
