# ImageQ API

Flask API for predicting classes made originally for [ImageQ](https://github.com/bisoncorps/imageQ)

[![Python flask](https://img.shields.io/badge/Python-flask-blue.svg)](https://http://flask.pocoo.org/)

![Docker Automated Build](https://img.shields.io/docker/automated/deven96/imageqapi.svg?style=flat)
![Docker Pulls](https://img.shields.io/docker/pulls/deven96/imageqapi.svg?style=flat)

[![Build Status](https://travis-ci.com/bisoncorps/imageQ_API.svg?branch=master)](https://travis-ci.com/bisoncorps/imageQ_API)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- [ImageQ API](#imageq-api)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
  - [Running Locally](#running-locally)
  - [Deploy](#deploy)
  - [Documentation](#documentation)
  - [Todo](#todo)

## Getting Started

Clone the repo

```bash
    # SSH
    git clone git@github.com:bisoncorps/imageQ_API.git
    # HTTPS
    git clone https://github.com/bisoncorps/imageQ_API.git
```

Activate virtual environment. All project work should be done in virtualenvs and virtualenv names must be added to gitignore

### Installation

- Install the requirements

```bash
    # install pipenv
    sudo pip3 install pipenv

    # install requirements
    pipenv install
```

## Running Locally

- With flask dev server

```bash
    python flask_api/run_keras_server.py
```

- With Gunicorn (port 8008)

```bash
    gunicorn -b :8008 flask_api:app
```

- With deployed Docker image from docker hub

```bash
    docker run deven96/imageqapi
```

Upon running image, docker container port is bound to [localhost](http://localhost:8008)

## Deploy

The `/predict` endpoint on `master` branch of the repo is linked to automatically deploy to be hosted on [Google Cloud](https://imageqapi.appspot.com/predict) and as a docker container `deven96/imageqapi`

## Documentation

Documentation including example use are available on [hosted version](https://imageqapi.appspot.com)

## Todo

See [TODO](TODO.md)