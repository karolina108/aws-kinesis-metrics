#!/usr/bin/env bash

aws cloudformation validate-template \
    --template-body file://kinesis-analytics/kinesis-application.yaml \
    --profile ${AWS_PROFILE}

aws cloudformation create-stack \
    --stack-name cs-aws-all-hmk-analytics-kinesis-app \
    --template-body file://kinesis-analytics/kinesis-application.yaml \
    --capabilities CAPABILITY_NAMED_IAM \
    --profile ${AWS_PROFILE}

aws cloudformation update-stack \
    --stack-name cs-aws-all-hmk-analytics-kinesis-app \
    --template-body file://kinesis-analytics/kinesis-application.yaml \
    --capabilities CAPABILITY_NAMED_IAM \
    --profile ${AWS_PROFILE}

aws cloudformation delete-stack \
    --stack-name cs-aws-all-hmk-analytics-kinesis-app \
    --profile ${AWS_PROFILE}