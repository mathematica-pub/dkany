from setuptools import find_packages
from setuptools import setup


setup(
    name='participant-data-request',
    version='0.0.1',
    description='participant-data-request',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)