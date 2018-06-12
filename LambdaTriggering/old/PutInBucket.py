import sys
import boto3
from botocore.client import Config
import random 
import datetime


# def genRandomImage():
# 	'''
# 	function to generate random image
# 	take in size as paramter later on
# 	'''
# 	dat = bytes([random.randint(1,3) for x in range(10000)])
# 	return Image.frombytes('1', (200,200), dat)



def putInBucket(access_key, secret_key, bucket_name):
	'''
	function to put data in bucket
	'''
	ACCESS_KEY_ID = access_key
	ACCESS_SECRET_KEY = secret_key
	BUCKET_NAME = bucket_name

	data = 'this is a test' #genRandomImage() # open(path_to_data, 'rb')

	s3 = boto3.resource(
	    's3',
	    aws_access_key_id=ACCESS_KEY_ID,
	    aws_secret_access_key=ACCESS_SECRET_KEY,
	    config=Config(signature_version='s3v4')
	)

	s3.Bucket(BUCKET_NAME).put_object(Key=str(datetime.datetime.now())+'.txt', Body=data)


if __name__ =='__main__':

	if len(sys.argv) != 4:
		print('Usage Error: /"python GetBuckets.py [access_key] [secret_key] [bucket_name]')
		sys.exit(1)

	putInBucket(sys.argv[1], sys.argv[2], sys.argv[3])

	print('Success')
