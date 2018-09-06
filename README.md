
[![Maintainability](https://api.codeclimate.com/v1/badges/0ef7545d395120222d77/maintainability)](https://codeclimate.com/github/andre-filho/commit-helper/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/595af9a088cf44e19ec2679a8c2617f6)](https://www.codacy.com/app/andre-filho/commit-helper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andre-filho/commit-helper&amp;utm_campaign=Badge_Grade)

# Commit Helper
---
## What does it do?
The commit-helper do exactly what it's name suggest: helps you create and maintain your commit policy by tailoring your commit message into a commit convention.

## Why should I use this?
Keeping a commit policy may sound like an easy thing to do, but in reality we both know that it isn't.

Sometimes we, the devs, go _full-loco_ while programming and make mistakes when commiting. That's fine, everyone makes mistakes. But, what if those mistakes could be avoided?

## Instalation
Just follow the commands below:

```bash

  # if you don't have git, run $ sudo apt install git first

  # clone the repo into your home
  $ git clone https://github.com/andre-filho/commit-helper.git ~/.commit-helper

  # create a function in your .bashrc
  $ echo "commit(){ python3 ~/.commit-helper/generator.py; }" >> ~/.bashrc

  # reload terminal
  $ source ~/.bashrc

```

## Project's maintainers
| **Name** | **Username** |
| :--------: | :-----: |
| André de Sousa Costa Filho | andre-filho |
