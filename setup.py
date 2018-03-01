from setuptools import setup, find_packages
from codecs import open
from os import path

from mezzy import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mezzy',
    version=__version__,
    description='Useful utilities for Mezzanine projects',
    long_description=long_description,
    url='https://gitlab.com/tigris-webdev/mezzy',
    author='Ed Rivas',
    author_email='e@jerivas.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='django mezzanine utility helper',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True
)
