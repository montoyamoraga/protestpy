# protest.py
# by montoyamoraga

# to distribute, on terminal do
# python setup.py sdist

from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='protest',
    version='0.5.11',
    url='https://github.com/montoyamoraga/protestpy',
    author='montoyamoraga',
    description='automatic generation of protesting material',
    long_description=long_description,
    license='MIT',
    packages= find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['Pillow', 'videogrep', 'selenium<3.0.0', 'youtube_dl', 'chromedriver'],
    package_data={'protest': ['*.ttf']}
)
