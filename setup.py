#!/usr/bin/env python
from setuptools import setup

kwargs = {}

with open('torn/version.py') as f:
    ns = {}
    exec(f.read(), ns)
    version = ns['version']

install_requires = ['tornado >= 6.0a1']


with open('README.rst') as f:
    kwargs['long_description'] = f.read()


python_requires = '>= 3.7'
kwargs['python_requires'] = python_requires

setup(
    name='torn',
    version=version,
    description='Torn - Tornado framework helper functions',
    url='https://github.com/glibin/torn',
    download_url='https://github.com/glibin/torn/tarball/{}'.format(version),
    packages=['torn', 'torn.test', 'torn.util'],
    install_requires=install_requires,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
    **kwargs
)
