from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Winery CahtGPT'
LONG_DESCRIPTION = 'Winery CahtGPT'

# Setting up
setup(
    name="Winerygpt",
    version=VERSION,
    author="Janvi Mehta",
    author_email="<jmehta@sigmasolve.net>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['langchain','chromadb','openai','tiktoken','python-dotenv'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
