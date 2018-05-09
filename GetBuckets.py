
import sys
import boto
import boto.s3.connection

"""
python script to print exiting buckets corresponding to an access/secret key pair
"""

def getBucket(access_key, secret_key):

	conn = boto.connect_s3(
		aws_access_key_id = access_key,
		aws_secret_access_key = secret_key,
		host = 'objects.dreamhost.com',
		is_secure=False,               # uncomment if you are not using ssl
		calling_format = boto.s3.connection.OrdinaryCallingFormat(),
		)

	for bucket in conn.get_all_buckets():
		print ("{name}\t{created}".format(
			name = bucket.name,
			created = bucket.creation_date,
		))

if __name__ =='__main__':

	if len(sys.argv) != 3:
		print('Usage Error: /"python GetBuckets.py [access_key] [secret_key]')
		sys.exit(1)

	getBucket(sys.argv[1], sys.argv[2])


