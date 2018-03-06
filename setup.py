from setuptools import setup
from setuptools import find_packages

setup(
    name='flask_demo',
    version='1',
    packages=find_packages(exclude=['tests']),
)
