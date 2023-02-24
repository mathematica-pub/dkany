from setuptools import find_packages
from setuptools import setup


setup(
    name='dkany',
    version='0.0.1',
    description='dkany',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires = [
        'pandas',
        'requests',
        'requests-toolbelt'
    ]
)