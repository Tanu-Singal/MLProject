#helps to build entire ML project into a package u can instll that package u can use it and can deploy on pypi so that anybody can use it
from setuptools import find_packages,setup
from typing import List
# find all the packages that are availble in entire ML application (find_package)
# setup.py = “installation instructions”

#Jaise:

#“Mera project install karna hai to ye-ye files lo, aur ye libraries bhi install karo”

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.strip() for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements


setup(
    name='mlProject',
    version='0.0.1',
    author='Tanu-Singal',
    author_email='tanusingal7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

#when find_packages() is running it will see how many folders have __init__.py and then consider that folder as a package itself like src and build it 
# and then u can import it anywhere like pandas seaborn and for that put in pypi package