#! /bin/bash

if [command -v git]; then
  sudo apt-get update -qq;
  sudo apt install git;
fi

if [command -v python3]; then
  sudo apt install python3;
fi

if [command -v pip3]; then
  sudo apt install python3-pip;
fi

git clone https://github.com/andre-filho/commit-helper.git ~/.commit-helper;

pip3 install --user ~/.commit-helper/requirements.txt;

chmod +x $HOME/.commit-helper/generator.py;

echo "commit(){ ./$HOME/.commit-helper/generator.py; }" >> $HOME/.bashrc;
