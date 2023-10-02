#!/bin/bash
set -eo pipefail

ARTIFACT_BUCKET=$(cat ./function-gateway/scripts/bucket-name.txt)
aws cloudformation package \
--template-file ./function-gateway/scripts/template.yml \
--s3-bucket $ARTIFACT_BUCKET \
--output-template-file ./function-gateway/scripts/out.yml

aws cloudformation deploy \
--template-file ./function-gateway/scripts/out.yml \
--stack-name ml-gateway \
--capabilities CAPABILITY_NAMED_IAM \
--parameter-overrides \
ScoringLambdaARN=arn:aws:lambda:us-east-1:819883234898:function:ml-scorer-function-8DxH1AHeW5x1 \
Phase=TST