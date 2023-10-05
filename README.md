# Flight Prediction
This repository contains an example of stateless function in Python.
It is made up of 2 functions:
- gateway
- scorer (this should interact with a ML model)

Both functions can be deployed in AWS as Lambda and Azure as FunctionApp.

## Status

### Build
* Prediction Gateway [![Build Gateway Function](https://github.com/dsanapo/flight-predictions/actions/workflows/build-gateway.yml/badge.svg?branch=main)](https://github.com/dsanapo/flight-predictions/actions/workflows/build-gateway.yml)
* Prediction Scorer [![Build Scorer Function](https://github.com/dsanapo/flight-predictions/actions/workflows/build-scorer.yml/badge.svg?branch=main)](https://github.com/dsanapo/flight-predictions/actions/workflows/build-scorer.yml)
### Deployment
* Prediction Gateway to AWS [![Deploy Gateway Function to AWS](https://github.com/dsanapo/flight-predictions/actions/workflows/deploy-gateway.yml/badge.svg?branch=main)](https://github.com/dsanapo/flight-predictions/actions/workflows/deploy-gateway.yml)
* Prediction Scorer to AWS [![Deploy Scorer Function to AWS](https://github.com/dsanapo/flight-predictions/actions/workflows/deploy-scorer.yml/badge.svg?branch=main)](https://github.com/dsanapo/flight-predictions/actions/workflows/deploy-scorer.yml)
* Deployment to Azure [![Deploy Gateway and Scorer Functions to Azure](https://github.com/dsanapo/flight-predictions/actions/workflows/deploy-gateway-azure.yml/badge.svg?branch=main)](https://github.com/dsanapo/flight-predictions/actions/workflows/deploy-gateway-azure.yml)

## Local development
### Virtual environment

You can create a python virtual environment using pyenv. 
You should create two different environments as there are 2 functions.
As example:
```bash
pyenv virtualenv 3.8.7 predictions-gateway-3.8.7
```

To automatically enable the environment
```bash
echo "predictions-gateway-3.8.7" > .python-version
```
### Install dependencies
```bash
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

### Checks
On each function you can perform the following checks:
* static code analysis
* static type analysis
* security issue
* unittests

Run the following commands:
```bash
flake8 function-gateway/src
mypy function-gateway/src
bandit function-gateway/src/*
pytest function-gateway/
```