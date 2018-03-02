# protest.py
# by aaron montoya-moraga
# march 2017

# to distribute, on terminal do
# python setup.py sdist

# from distutils.core import setup

from setuptools import *
from codecs import open
from os import path


# taken from https://tom-christie.github.io/articles/pypi/
here = path.abspath(path.dirname(__file__))

# taken from https://tom-christie.github.io/articles/pypi/
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='protest',
    version='0.5.10',
    url='https://github.com/montoyamoraga/protestpy',
    author='aaron montoya-moraga',
    description='automatic generation of protesting material',
    long_description=long_description,
    license='MIT',
    packages= find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['Pillow', 'videogrep', 'selenium<3.0.0', 'youtube_dl', 'chromedriver'],
    package_data={'protest': ['*.ttf']}
)
