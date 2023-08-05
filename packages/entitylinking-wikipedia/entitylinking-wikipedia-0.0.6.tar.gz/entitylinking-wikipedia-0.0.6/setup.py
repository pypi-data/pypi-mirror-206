from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION_FILE = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION='Package for Entity Linking using WikiPedia'
# LONG_DESCRIPTION = file:README.md
URL = 'https://github.com/pypa/sampleproject'

#Setting Up
setup(
    name='entitylinking-wikipedia',
    version=VERSION,
    author='Soumyadipta Maiti',
    author_email='soumya55555@gmail.com',
    description=DESCRIPTION,
    long_description = LONG_DESCRIPTION_FILE,
    long_description_content_type = "text/markdown",
    url= URL,
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