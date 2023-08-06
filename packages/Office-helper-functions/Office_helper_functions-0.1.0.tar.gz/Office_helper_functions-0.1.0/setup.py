from setuptools import find_packages, setup
setup(
    name='Office_helper_functions',
    packages=find_packages(),
    version='0.1.0',
    description='Helper functions for Microsoft Office',
    author='Andreas Löfkvist',
    author_email='andreas.lofkvist@greenlandscaping.se',
    license='MIT',
    setup_requires=['beautifulsoup4']
)