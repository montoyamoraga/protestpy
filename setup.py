#protest.py
#by aaron montoya-moraga
#march 2017

#to distribute, on terminal do
#python setup.py sdist

#from distutils.core import setup
from setuptools import *

setup(
    name='protest',
    version='0.3.9',
    url='https://github.com/montoyamoraga/protestpy',
    author='aaron montoya-moraga',
    description='automatic generation of protesting material',
    license='MIT',
    packages= find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['Pillow', 'videogrep', 'selenium', 'youtube_dl'],
    package_data={'protest': ['*.ttf']}
)
