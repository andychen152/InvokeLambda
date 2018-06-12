import os
import platform
import boto3
from botocore.client import Config
import datetime

def putInBucket():
    '''
    function to put data in bucket
    '''
    ACCESS_KEY_ID = <access_key>
    ACCESS_SECRET_KEY = <secret_key>
    BUCKET_NAME = <bucket_name>

    data = 'this is a test' # initial data, change as we test different sizes and data types

    s3 = boto3.resource(
            's3',
                aws_access_key_id=ACCESS_KEY_ID,
                aws_secret_access_key=ACCESS_SECRET_KEY,
                config=Config(signature_version='s3v4')
            )

    s3.Bucket(BUCKET_NAME).put_object(Key=str(datetime.datetime.now())+'.txt', Body=data)

putInBucket()

message = "Using Python '{0}'".format(platform.python_version())
print(message)
