from setuptools import setup
from codecs import open
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

setup(
    name='solfinder',
    version='1.0',
    packages=['solfinder'],
    url='',
    license='GNU',
    author='fcastino',
    author_email='f.castino@tudelft.nl',
    description='SolFinder 1.0',
    long_description_content_type="text/markdown",
    long_description=long_description,
    include_package_data=True,
    install_requires=["numpy", "matplotlib"]
)
