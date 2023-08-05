#!/usr/bin/env python
# coding: utf-8

from setuptools import Extension, setup
from setuptools import dist
from distutils.core import setup

dist.Distribution().fetch_build_eggs(['Cython>=0.15.1', 'numpy>=1.10'])

import numpy as np 
from Cython.Build import cythonize

from pathlib import Path
this_directory = Path(__file__).parent

long_description = (this_directory / "README.md").read_text()

extensions = Extension(
    "tuotuo/cutils", 
    ["tuotuo/cutils.pyx"],
    include_dirs=[np.get_include()], 
)

setup(
    name = 'TuoTuo',
    packages = ['tuotuo'],
    version = '0.1.2',  
    license='MIT',
    description = 'LDA & Neura based topic modelling library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'tuotuo Superman',
    author_email = 'tuotuo@HanwellSquare.BigForce.com',
    url = 'https://github.com/RobbenRibery/TuoTuo',
    download_url = 'https://github.com/RobbenRibery/TuoTuo/archive/refs/tags/Pypi-0.0.5.tar.gz',
    keywords = ['Generative Topic Modelling','Latent Dirichlet Allocation'],
    install_requires=[            
        'numpy',
        'torch',
        'scipy',
        'pyro-ppl',
        'pandas',
        'nltk',
        'spacy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
  ],
    ext_modules=cythonize(extensions, annotate=True),
)