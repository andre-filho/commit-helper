from setuptools import setup

setup(
    name = 'commit-helper',
    version = '3.0.0',
    packages = ['commit_helper'],
    entry_points = {
        'console_scripts': [
            'commit = commit_helper.__main__:main'
        ]
    }
)
