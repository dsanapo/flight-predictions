#!/bin/bash
set -eo pipefail

ARTIFACT_BUCKET=$(cat ./function-scorer/scripts/bucket-name.txt)
aws cloudformation package \
--template-file ./function-scorer/scripts/template.yml \
--s3-bucket $ARTIFACT_BUCKET \
--output-template-file ./function-scorer/scripts/out.yml

aws cloudformation deploy \
--template-file ./function-scorer/scripts/out.yml \
--stack-name ml-scorer \
--capabilities CAPABILITY_NAMED_IAM