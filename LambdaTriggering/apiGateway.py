'''
calls apigateway
'''

import platform
import requests

def callAPI():
    url = <api_endpoint>
    ret = requests.get(url)


callAPI()

message = "Using Python '{0}'".format(platform.python_version())
print(message)
