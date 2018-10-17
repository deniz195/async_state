# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='async_state',
    version='0.1.0',
    description='A synchronization primitive that represents a state of a state machine and allows to access it using async/await syntax.',
    long_description=readme,
    author='Deniz Bozyigit',
    author_email='deniz195@gmail.com',
    url='https://github.com/deniz195/async_state',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
