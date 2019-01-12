<p align="center">
  <img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/200-200.png" style="align: center">
  <h1 align="center">Commit Helper</h3>
</p>

<p align="center">
  <a href="https://travis-ci.org/andre-filho/commit-helper">
    <img src="https://travis-ci.org/andre-filho/commit-helper.svg?branch=master" alt="Build Status">
  </a>
  <a href="https://codeclimate.com/github/andre-filho/commit-helper/maintainability">
    <img src="https://api.codeclimate.com/v1/badges/0ef7545d395120222d77/maintainability" alt="Maintainability">
  </a>
  <a href="https://codebeat.co/projects/github-com-andre-filho-commit-helper-master"><img alt="codebeat badge" src="https://codebeat.co/badges/7621c6dc-7143-4efa-af3e-45508210d276" /></a>
  <a href="https://www.codacy.com/app/andre-filho/commit-helper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andre-filho/commit-helper&amp;utm_campaign=Badge_Grade">
    <img src="https://api.codacy.com/project/badge/Grade/595af9a088cf44e19ec2679a8c2617f6" alt="Codacy Badge">
  </a>
  <a href="https://codeclimate.com/github/andre-filho/commit-helper/test_coverage"><img src="https://api.codeclimate.com/v1/badges/0ef7545d395120222d77/test_coverage" /></a>
  <a class="badge-align" href="https://www.codacy.com/app/andre-filho/commit-helper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andre-filho/commit-helper&amp;utm_campaign=Badge_Coverage">
    <img src="https://api.codacy.com/project/badge/Coverage/595af9a088cf44e19ec2679a8c2617f6"/>
  </a>
</p>

## What does it do?
The commit-helper do exactly what it's name suggest: helps you create and maintain your commit policy by tailoring your commit message into a commit convention.

## Why should I use this?
Keeping a commit policy may sound like an easy thing to do, but in reality we both know that it isn't.

Sometimes we, the developers, go _full-loco_ while programming and make mistakes when commiting. That's fine, everyone makes mistakes. But, what if those mistakes could be avoided?

## Screenshots

### Initial commit

<img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/gifs/generate-file.gif" style="min-width:200px;margin-left:auto;margin-right:auto;"/>

### Normal commit

<img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/gifs/commit.gif" style="min-width:200px;margin-left:auto;margin-right:auto;"/>

### Commit without generating a configuration file

<img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/gifs/--no-file.gif" style="min-width:200px;margin-left:auto;margin-right:auto;"/>

### Co-authored commit

<img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/gifs/co-author.gif" style="min-width:200px;margin-left:auto;margin-right:auto;"/>

### Fast commit

<img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/gifs/single-line.gif" style="min-width:200px;margin-left:auto;margin-right:auto;"/>

### Debugging and commiting

<img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/gifs/--debug.gif" style="min-width:200px;margin-left:auto;margin-right:auto;"/>

### All-in-one commit

<img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/gifs/all.gif" style="min-width:200px;margin-left:auto;margin-right:auto;"/>

### Help

<img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/gifs/flag-h.gif" style="min-width:200px;margin-left:auto;margin-right:auto;"/>

### Getting help for writing in a convention

<img src="https://raw.githubusercontent.com/andre-filho/commit-helper/master/assets/gifs/tag-help.gif" style="min-width:200px;margin-left:auto;margin-right:auto;"/>

## Installation

In order to install one of our older versions, check our [previous releases](PREVIOUS_VERSIONS). To install the latest (pip) version, just follow the commands below:

```bash
$ pip3 install commit-helper
```

## Updating your current version

If you already have one of our `pip` releases installed in your machine and want to update to the latest version, use the command:

```bash
$ pip3 install --upgrade commit-helper
```

## Usage and configuration

This program has a cli that you can take advantage of. Running `commit --help`
will show you the usage and options for your commit. All of them are optional
for the sake of not losing your precious time.

```bash
 $ commit -h
usage: commit [-h] [-t TAG] [-m MESSAGE] [-ct CONTEXT] [-ca CO_AUTHOR] [-nf]
              [-c {angular,karma,tagged,symphony,message}] [-d]

A commit formatter tool to help you follow commit conventions.

optional arguments:
  -h, --help            show this help message and exit
  -t TAG, --tag TAG     Pass your commit tag directly
  -m MESSAGE, --message MESSAGE
                        Pass your commit message directly
  -ct CONTEXT, --context CONTEXT
                        Pass your commit context directly
  -ca CO_AUTHOR, --co-author CO_AUTHOR
                        Make your friend an co-author to the commit
  -nf, --no-file        Disables the creation of a commiter.yml or commit-helper.yml file
  -c {angular,karma,tagged,symphony,message}, --convention {angular,karma,tagged,symphony,message}
                        Selects a convention to be used for the commit.
                        Required if there's no commiter.yml or commit-helper.yml file.
  -d, --debug           Toggles debug option

```

So, if you want to write a co-authored commit, you should use:

```bash
$ commit --co-author "foo bar doritous <foobar@douritos.com>"
```

Or if you are using this for the first time in your project:

```bash
$ commit --convention tagged
```

To work even more smoothly, have in your working directory a file named **commiter.yml or commit-helper.yml**. In this file you must pass the commit convention that you want to use, following the example:

```yaml
convention: angular   # tag(context): commit message

# or

convention: karma   # tag(context): commit message

# or

convention: tagged # TAG: commit message

# or

convention: symphony  # [Tag] commit message

# and if you're feeling adventurous

convention: none      # Commit message
```

In case that you or your organization does already have a commit convention that is not listed above, you can configure it in the commiter.yml or commit-helper.yml file as following:

```yaml
convention: custom
# considering a commit message like '{add} (stuff) ~> in file foo.br'
commit_pattern: '{tag} (context) ~> message'
# tag, message and context are reserved words that will be replaced in your commit message
context: true # this is a must have field! If your pattern doesn't have one, assign false to it
```

Supported conventions available:

 - angular
 - karma
 - tagged
 - symphony
 - atom
 - only message (no convention)
 - a custom one that you may create :)

 ## Troubleshooting
 If after you've installed commit-helper the `commit` or `commit-helper` commands are not usable at the command line, check if `$HOME/.local/bin` is on your PATH. If not, add it on your .bashrc file by running:
 ``` bash
$ echo "export PATH=$HOME/.local/bin:$PATH" >> .bashrc
 ```

## Project's maintainers
| **Name** | **Username** |
| :--------: | :-----: |
| André de Sousa Costa Filho | @andre-filho |

## Our collaborators
| **Name** | **Username** |
| :------: | :----------: |
| Arthur José Benedito de Oliveira Assis | @arthur0496 |
| Matheus Richard Torres Gomes de Melo | @MatheusRich |
