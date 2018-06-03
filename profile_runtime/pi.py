import requests
import json


def CreateInput(inputs):
	n = len(inputs)
	ret = [[0]*2 for _ in xrange(n)]

	# AWS & GCP
	for i in xrange(n):
		ret[i][0] = json.dumps({"iter":inputs[i]})

	# Azure
	for i in xrange(n):
		ret[i][1] = json.dumps({"num":inputs[i]})
	
	return ret


nums = [
	100000, 
	1000000, 
	10000000, 
	100000000
	]
NUM_TESTS = 50

URLS = {
	"GCP": "https://us-central1-bold-script-204219.cloudfunctions.net/calculate_pi",
	"AWS": "https://ajkxgtlsxf.execute-api.us-west-1.amazonaws.com/prod/pi",
	"Azure": "https://computepi.azurewebsites.net/api/HttpTriggerJS1?code=dop/aTm6SCDIyAaudKn25mY85pczrZOft630FOFu4uzxPBxiuIGkxw=="
}

avgs = {
	"GCP": [0.0]*len(nums),
	"AWS": [0.0]*len(nums),
	"Azure": [0.0]*len(nums)
}


inputs = CreateInput(nums)

for i, put in enumerate(inputs):
	for _ in xrange(NUM_TESTS):
		for platform in URLS:
			# val is used for two purposes, one to index put, and another to store time
			val = 0
			headers = {'Content-Type': 'application/json'}
			if platform == "Azure":
				val = 1

			r = requests.post(URLS[platform], headers=headers, data=put[val])
			if platform == "GCP":
				val = int(r.text)
			else: # platform in ["AWS", "Azure"]:
				val = int(r.text[1:-1])

			avgs[platform][i] += val

for platform in avgs:
	print platform
	for i, val in enumerate(avgs[platform]):
		print "test:", i, ":", val/NUM_TESTS
