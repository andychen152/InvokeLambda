from __future__ import print_function
import boto3
import os
import sys
import uuid
     
s3_client = boto3.client('s3')
     
def reverse_string(string_path, reversed_path):
    with open(string_path, 'r') as fd_read:
        with open(reversed_path, 'w') as fd_write:
            for line in fd_read:
                line = str(line.strip()[::-1]) + "\n"
                fd_write.write(line)

     
def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key'] 
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/reverse-{}'.format(key)
        
        s3_client.download_file(bucket, key, download_path)
        reverse_string(download_path, upload_path)
        s3_client.upload_file(upload_path, '{}reverse'.format(bucket), key)
