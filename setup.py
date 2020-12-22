# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------------
# Load modules
# --------------------------------------------------------------------------------

import os, sys
from setuptools import setup, find_packages



# --------------------------------------------------------------------------------
# read files
# --------------------------------------------------------------------------------

# get current working directory
# current_path = os.path.abspath(os.path.dirname(__file__))

# read files

# requirements.txt
# requirements_path = os.path.join(current_path, 'requirements.txt')
requirements_path = './requirements.txt'
with open(file=requirements_path, mode='r', encoding='utf-8') as f:
    requirements_list = f.readlines()

# README.rst
# readme_path = os.path.join(current_path, 'README.rst')
readme_path = './README.rst'
with open(file=readme_path, mode='r', encoding='utf-8') as f:
    readme_txt = f.read()

# LICENSE
# license_path = os.path.join(current_path, 'LICENSE')
license_path = './LICENSE'
with open(file=license_path, mode='r', encoding='utf-8') as f:
    license_txt = f.read()



# --------------------------------------------------------------------------------
# setup
# --------------------------------------------------------------------------------

setup(
    name='sample_annn_pkg',
    version='0.0.13',
    description='sample_annn_pkg description',
    long_description=readme_txt,
    author='hoge',
    author_email='fuga@email.com',
    install_requires=requirements_list,
    url='',
    license=license_txt,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)

