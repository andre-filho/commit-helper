from setuptools import setup

with open("README.md", 'r') as fi:
    long_desc = fi.read()

setup(  # pragma: no cover
    name='commit-helper',
    description="A python program that helps you write commits following commit conventions",  # nopep8
    url='https://github.com/andre-filho/commit-helper',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Andre de Sousa Costa Filho',
    author_email='andre.filho001@outlook.com',
    version='3.0.1',
    packages=['commit_helper'],
    entry_points={
        'console_scripts': [
            'commit = commit_helper.__main__:main',
            'commit-helper = commit_helper.__main__:main',
        ]
    },
    install_requires=[
        'pyyaml',
        'argparse',
    ],
)
