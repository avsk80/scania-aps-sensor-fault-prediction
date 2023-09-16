from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirements_list: List[str] = []
    with open('requirements.txt') as f:
        requirements_list = f.read().splitlines()
    return requirements_list

setup(
    name='sensor',
    version='0.0.1',
    author='avsk',
    author_email='avskkrish80@gmail.com',
    packages=find_packages(),
    install_requires=[],
)
