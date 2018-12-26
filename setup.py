import os
import codecs
from os import path
from setuptools import setup
from setuptools import find_packages
from pip._internal.req import parse_requirements

here = path.abspath(path.dirname(__file__))

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allowes setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# parse_requirements() returns generator of pip.req.InstallRequirement objects
INSTALL_REQS = parse_requirements('requirements.txt', session='hack')

# reqs is a list of requirements
REQUIREMENTS = [str(ir.req) for ir in INSTALL_REQS]

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: Portuguese",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(  # pragma: no cover
    name='commit-helper',
    description="A python program that helps you write commits following commit conventions",  # nopep8
    url='https://github.com/andre-filho/commit-helper',
    long_description=codecs.open('README.md', 'rb', 'utf8').read(),
    long_description_content_type='text/markdown',
    author='Andre de Sousa Costa Filho',
    author_email='andre.filho001@outlook.com',
    version=codecs.open('VERSION.txt', 'rb', 'utf8').read(),
    packages=find_packages(),
    keywords=['commit', 'helper', 'git', 'version', 'versioning'],
    entry_points={
        'console_scripts': [
            'commit = commit_helper.__main__:main',
            'commit-helper = commit_helper.__main__:main',
        ]
    },
    install_requires=REQUIREMENTS,
    license='GNU',
    classifiers=CLASSIFIERS,
)
