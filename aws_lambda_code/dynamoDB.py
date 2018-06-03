import boto.ses
import boto.dynamodb2
from boto.dynamodb2.table import Table
import random

'''
code triggers lambda by MODIFYING item in table
pre: item already in table
'''
conn = boto.dynamodb2.connect_to_region(
    <region>,
    aws_access_key_id=<access_key>, 
    aws_secret_access_key=<secret_key>, 
)

users = Table(<table_name>, connection =conn)

item = users.get_item(<existing_user>)
item["first_name"] = <first_name>
item["last_name"] = str(random.randint(0,1000000)) # must be different to overwrite

item.save(overwrite=True)
