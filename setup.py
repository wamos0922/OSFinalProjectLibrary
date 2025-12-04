# setup.py
from setuptools import setup, find_packages

setup(
    name='ossimg',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow', # Required dependency for your image functions
    ],
)