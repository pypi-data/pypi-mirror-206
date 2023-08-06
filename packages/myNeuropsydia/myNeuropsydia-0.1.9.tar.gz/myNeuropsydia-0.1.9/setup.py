# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup( 
    name='myNeuropsydia',
    packages=find_packages(),
    version='0.1.9', 
    description='Partially fixed version of Neuropsydia library, a Python module for creating experiments, tasks and questionnaires',
    author='Laborde',
    license='ENS_Paris_Saclay',
    package_data = {
                	"Neuropsydia.files.font":["*.ttf", "*.otf"],
                	"Neuropsydia.files.binary":["*.png"],
                	"Neuropsydia.files.logo":["*.png"]},
    install_requires=['Pillow',
                      'cryptography',
                      'neurokit',
                      'numpy',
                      'pandas',
                      'pygame==2.1.2',
                      'python-docx',
                      'pyxid',
                      'statsmodels'],
)


