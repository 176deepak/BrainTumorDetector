'''
This file is used for describing metadata about project and installing this project as local module in system with all its dependencies using pip tool.

setup.py file store all metadata about project as egg form.
'''


from setuptools import setup, find_packages
from typing import List

# editable mode 
HYPEN_E_DOT = '-e .'


# extracting all required packages for project from requirements.txt file 
'''
returns list of packages

'''
def get_requirements(file_path:str) -> List[str]: 
    required_modules = []
    with open(file_path) as file_reader:
        modules = file_reader.readlines()
        required_modules = [module.replace('\n', '') for module in modules]
    
    if HYPEN_E_DOT in required_modules:
        required_modules.remove(HYPEN_E_DOT)
    
    return required_modules


setup(
    name="TumorDetector",
    version="0.0.1",
    author="Deepak",
    author_email="deepak170602@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)