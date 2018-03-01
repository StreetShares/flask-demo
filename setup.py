from setuptools import setup
from setuptools import find_packages

setup(
    name='syncmachine_flask',
    version='1',
    packages=find_packages(exclude=['tests']),
)
