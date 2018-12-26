#!/bin/bash

docker run --tty --interactive --volume $PWD:/commit-helper --name commit-helper --workdir /commit-helper python:3.6 bash