#!/bin/bash
set -eo pipefail

ARTIFACT_BUCKET=$(cat ./function-gateway/scripts/bucket-name.txt)
aws cloudformation package --template-file ./function-gateway/scripts/template.yml --s3-bucket $ARTIFACT_BUCKET --output-template-file ./function-gateway/scripts/out.yml
aws cloudformation deploy --template-file ./function-gateway/scripts/out.yml --stack-name ml-gateway --capabilities CAPABILITY_NAMED_IAM
