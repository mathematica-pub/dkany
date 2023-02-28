from setuptools import find_packages
from setuptools import setup
import os


# TODO force the version to be consistent with git tag
setup(
    name='dkany',
    version="0.0.7",
    description='dkany',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires = [
        'pandas',
        'requests',
        'requests-toolbelt'
    ]
)