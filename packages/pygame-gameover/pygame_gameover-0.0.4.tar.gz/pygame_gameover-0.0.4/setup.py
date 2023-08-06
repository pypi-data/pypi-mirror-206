import pathlib
from setuptools import setup

from setuptools import setup, find_packages
import codecs
import os

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pygame_gameover",
    version="0.0.4",
    description="It game gameover module",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kurban-hussain-786/MY-CODE",
    author="kurban hussain",
    author_email="kurbanhussain086@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords=['gameover in pygame','pygame gameover','gameover','over game','game over','pygame_gameover','gameover_pygame','pygame game','pygame','pygame GAMEOVER'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    
    
    
    
)
