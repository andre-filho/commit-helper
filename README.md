
[![Maintainability](https://api.codeclimate.com/v1/badges/0ef7545d395120222d77/maintainability)](https://codeclimate.com/github/andre-filho/commit-helper/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/595af9a088cf44e19ec2679a8c2617f6)](https://www.codacy.com/app/andre-filho/commit-helper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andre-filho/commit-helper&amp;utm_campaign=Badge_Grade)

# Commit Helper
## What does it do?
The commit-helper do exactly what it's name suggest: helps you create and maintain your commit policy by tailoring your commit message into a commit convention.

## Why should I use this?
Keeping a commit policy may sound like an easy thing to do, but in reality we both know that it isn't.

Sometimes we, the developers, go _full-loco_ while programming and make mistakes when commiting. That's fine, everyone makes mistakes. But, what if those mistakes could be avoided?

## Installation

Just follow the commands below:

```bash

  # make sure you have the dependencies installed in your machine and
  # have git ready to use

  $ sudo apt install python3-pip git

  $ pip3 install pyyaml

  # clone the repo into your home
  $ git clone https://github.com/andre-filho/commit-helper.git ~/.commit-helper

  # create a function in your .bashrc
  $ echo "commit(){ python3 ~/.commit-helper/generator.py; }" >> ~/.bashrc

  # reload terminal
  $ source ~/.bashrc

```

## Usage and configuration

For this project to work smoothly, you must have in your working directory a file named **commiter.yml**. In this file you must pass the commit convention that you want to use, following the example:

```yaml
convention: angular   # tag(context): commit message

# or

convention: changelog # TAG: commit message

# or

convention: symphony  # [Tag] commit message

# and if you're feeling adventurous

convention: none      # Commit message
```



Supported conventions available:
<!-- list here all tags that are used in configuration file -->

 - angular/karma
 - changelog
 - symphony

In the event of no commiter.yml file presence, you will be prompted with the following option menu:

```bash
No config files found!
Running default script...
    what type of commit convention are you using?

    (default): No convention
    1: Karma/Angular
    2: Conventional changelog
    3: Symfony CMF

```



## Project's maintainers
| **Name** | **Username** |
| :--------: | :-----: |
| André de Sousa Costa Filho | @andre-filho |
