# AWS Lambda Trigger
This directory contains the files needed to trigger Lambda from Azure.

## Setting up Lambda
You will need to set up IAM and connect all AWS services correctly so Lambda will have read and write permissions to the destination S3 bucket as well as the respected triggers. Then you can deploy the image resizing and string reversing code located in ```/Lambda```

## Setting up Azure
Create three different Azure functions and deploy the three code located in ```/Azure```. Save the http link for each deployed function. 

## Running Trigger
Simply run ```python main.py``` after filling out the respected http trigger link within the code.