from setuptools import setup, find_packages
import codecs
import os
VERSION = '0.0.2'
DESCRIPTION='Package for Entity Linking using WikiPedia'

#Setting Up
setup(
    name='entitylinking_wikipedia',
    version=VERSION,
    author='Soumyadipta Maiti',
    author_email='soumya55555@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'spacy','spacy_entity_linker'],
    keywords=['Python','Entity Linking', 'NER', 'WikiPedia'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]

)