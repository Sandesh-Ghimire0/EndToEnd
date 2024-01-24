'''
It is essential for creating machine learning application as a package.
It contains metadata about the project, such as the project's name, version, author, description, and other information.

'''

from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    # this function will return the list of all the packages from requirements.txt(file_path)
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n','') for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name='end to end mlproject',
    version='0.0.1',
    author='sandesh',
    author_email='sandeshghimire100@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)