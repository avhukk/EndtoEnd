## To convert the folders into packages
from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]: 
    requirements = []
    with open(file_path) as file_obj: 
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements

setup (
    name = 'src', 
    version = '0.0.1', 
    author = 'Abhishek', 
    author_email= 'avhukkerikar@gmail.com', 
    install_requires = ['numpy', 'pandas', 'matplotlib', 'Flask'],
    packages = find_packages()
)