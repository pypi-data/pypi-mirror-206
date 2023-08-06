from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'pygame_gameover to perfrm gameover'
loag_descciptionss=os.path.join("C:\\Users\\Lenovo\\Desktop\\pygame package gameover\\README.MD")

# Setting up
setup(
    name="pygame_gameover",
    version=VERSION,
    author="kurban hussain",
    author_email="kurbanhussain086@gmail.com",
    description=DESCRIPTION,
    long_description=  loag_descciptionss,
    long_description_content_type="text/markdown",
    
    packages=find_packages(),
    install_requires=["pygame","os","sys","mixer"],
    keywords=['pygame_gameover', 'gameover', 'game over', 'python tutorial', 'kurban hussain','game over in python','gameover_pygame','game over pygame','over game'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)