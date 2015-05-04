#!/usr/bin/env python

from setuptools import setup, find_packages

version = '1.0'

setup(
    name='i2a',
    version=version,
    description='i2a creates ASCII art from images right on your terminal.',
    long_description=open('README.rst').read(),
    author='Sid Verma',
    author_email='sid@sidverma.net',
    license='MIT',
    keywords=['image','jpg','ascii','art'],
    url='http://github.com/mavidser/i2a',
    packages=['i2a'],
    install_requires=[
        'docopt>=0.6.2',
        'Pillow>=2.5.0'
    ],
    entry_points={
        'console_scripts': [
            'i2a=i2a.i2a:main'
        ],
    }
)
