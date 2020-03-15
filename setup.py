from setuptools.command.build_ext import build_ext

import sys
import os
import glob
import setuptools

__version__ = '1.0.0'


        
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='publish_test',
    version=__version__,
    license='GPL 3.0',
    description='Auxiliary package just to test automatic release using Github actions.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Jan Brezina',
    author_email='jan.brezina@tul.cz',    
    url='https://github.com/geomop/test_publish',
    download_url='https://github.com/geomop/bgem/archive/v{__version__}0.1.0.tar.gz',
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers        
        'Development Status :: 2 - Pre-Alpha',
    ],
    
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    
    packages=['publish_test'],
    python_requires='>=3',
)        
        
        
        
