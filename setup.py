from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path):
    '''
    This function will return the list of requirements 
    '''
    requirements = []
    with open(file_path) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove('-e .')
    
    return requirements
        
setup(
    name="Student_Marks_Prediction",
    version = '0.0.1',
    author = 'Sachin Poojary',
    author_email = 'sachinpoojary0087@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)