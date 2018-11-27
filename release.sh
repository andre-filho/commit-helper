#! /bin/bash

python3 setup.py sdist bdist_wheel

if [ "$1" == "test" ]; then
  twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose
fi

if [ "$1" == "deploy" ]; then
  twine upload dist/* --verbose
fi
