[![Build Status](https://travis-ci.org/andre-filho/commit-helper.svg?branch=master)](https://travis-ci.org/andre-filho/commit-helper)
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

  # clone the repo into your home
  $ git clone https://github.com/andre-filho/commit-helper.git ~/.commit-helper

  $ pip3 install -r ~/.commit-helper/requirements.txt

  # create a function in your .bashrc
  $ echo "alias commit='python3 ~/.commit-helper/generator.py'" >> ~/.bashrc

  # reload terminal
  $ source ~/.bashrc
```

## Usage and configuration

This program has a cli that you can take advantage of. Running `commit --help`
will show you the usage and options for your commit. All of them are optional
for the sake of not losing your precious time.

```bash
  $ commit -h
  usage: generator.py [-h] [--co-author CO_AUTHOR] [--no-generate NO_FILE]
                    [--convention {angular,changelog,symphony,message}]

  A commit formatter tool to help you follow commit conventions.

  optional arguments:
    -h, --help            show this help message and exit
    --co-author CO_AUTHOR
                          make your friend an co-author to the commit
    --no-generate NO_FILE
                          disables the creation of a commiter.yml file
    --convention {angular,changelog,symphony,message}
                          Selects a convention to be used for the commit.
                          Required if there is no commiter.yml file.
```

So, if you want to write a co-authored commit, you should use:

```bash
$ commit --co-author "foo bar doritous <foobar@douritos.com>"
```

Or if you are using this for the first time in your project:

```bash
$ commit --convention changelog
```

To work even more smoothly, have in your working directory a file named **commiter.yml**. In this file you must pass the commit convention that you want to use, following the example:

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

 - angular/karma
 - changelog
 - symphony


## Project's maintainers
| **Name** | **Username** |
| :--------: | :-----: |
| André de Sousa Costa Filho | @andre-filho |

## Our collaborators
| **Name** | **Username** |
| :------: | :----------: |
| Arthur José Benedito de Oliveira Assis | @arthur120496 |
