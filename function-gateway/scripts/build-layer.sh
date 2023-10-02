#!/bin/bash

set -eo pipefail
rm -rf ./function-gateway/package
pip3 install --target ./function-gateway/package/python -r ./function-gateway/requirements.txt