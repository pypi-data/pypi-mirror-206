from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'FIS calculator for neurological protein-protein interactions'
LONG_DESCRIPTION = 'The Functional Interactomes Score (FIS) calculator is a library that allows you to quantify the strength of your neurological protein-protein interactions as described by in the FIABS approach'

# Setting up
setup(
    name="fis_calculator",
    version=VERSION,
    author="Neural Dynamics Group",
    author_email="<shreyankkadadi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    keywords=['python', 'neuroscience', 'protein-protein', 'biology'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)