# dhuolib

![Version](https://img.shields.io/badge/version-0.1.5-blue.svg?cacheSeconds=2592000)
[![License: MIT](https://img.shields.io/badge/License-MIT-grenn.svg)](#)

> Library for data science on DHuO Data 

### 🏠 [Homepage](https://gitlab.engdb.com.br/dhuo-plat/dhuo-data/data-science/dhuolib)

## Install


`dhuolib` supports Python 3.8 and higher.

### System-wide or user-wide installation with pipx

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `dhuolib`.

```sh
$ pip install dhuolib
```

## Usage

Login at DHuO Platform

```sh
    # create /.dhuo config file
    $ dh login
```

```sh
    # /.dhuo (config file example)

    [default]
    username = email@test.com
    password = xpto
    project = 
    workspace = 9iS36lMPQXWwAmgAVk
    workspace_id = 
    experiment_id = 
```


Help Login

```sh
    $ dh login --help

    Usage: dh login [OPTIONS]

    Provides user authentication

    Options:
    --email TEXT         Your DHuO Data email
    --password TEXT      Your DHuO Data password
    --env [prd|dev|stg]  Specify environment
    --help               Show this message and exit.
```
