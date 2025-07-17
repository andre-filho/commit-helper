import os
import codecs
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('VERSION.txt', encoding='utf-8') as f:
    version = f.read().strip()

# allowes setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# load requirements
with open('requirements.txt') as f:
    REQUIREMENTS = [line.strip() for line in f if line.strip() and not line.startswith('#')]


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
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Andre de Sousa Costa Filho',
    author_email='andre.filho001@outlook.com',
    version=version,
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
