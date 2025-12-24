from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    requirements: List[str] = []
    with open(file_path, 'r', encoding='utf-8') as file_obj:
        requirements = [line.strip() for line in file_obj if line.strip()]
    return requirements


setup(
    name='Recommend a movie',
    version='0.0.1',
    author='Priyanshu Mallick',
    author_email='priyanshumallick04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
