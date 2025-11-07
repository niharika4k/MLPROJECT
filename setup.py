#I will be able to build entire ml pipeline as a package using setup.py
from setuptools import setup, find_packages
from typing import List

#Instead of defining the packages, we ask to pick them from requirements file through this function
HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] #To replace n with space

        # To remove -e. from requirements to the setup.py file
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        


setup(
    name='MLPROJECT',          # your project/package name
    version='0.0.1',                # project version
    author='nihar',
    author_email='niharika4k@gmail.com',
    description='End-to-end machine learning project',
    packages=find_packages(),       # automatically include all packages with __init__.py
    install_requires=get_requirements('requirements.txt')
           # or your environment’s version
)