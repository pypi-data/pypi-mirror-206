from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'pygame_gameover is perfrom gameover'
LONG_DESCRIPTION = 'gameover pygame module'

# Setting up
setup(
    name="pygame_gameover",
    readme='README.MD',
    version=VERSION,
    author="kurban hussain",
    author_email="kurbanhussain086@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['gameover in pygame','pygame gameover','gameover','over game','game over','pygame_gameover','gameover_pygame','pygame game','pygame','pygame GAMEOVER'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)