import requests
import json


def CreateInput(inputs):
	n = len(inputs)
	ret = [[0]*2 for _ in xrange(n)]

	# AWS & GCP
	for i in xrange(n):
		ret[i][0] = json.dumps({"n":inputs[i]})

	# Azure
	for i in xrange(n):
		ret[i][1] = json.dumps({"num":inputs[i]})
	
	return ret


nums = [100, 200, 300, 400]
NUM_TESTS = 1

URLS = {
	"GCP": "https://us-central1-bold-script-204219.cloudfunctions.net/spectral_norm",
	"AWS": "https://ajkxgtlsxf.execute-api.us-west-1.amazonaws.com/prod/spectral",
	"Azure": "https://azurespecnorm.azurewebsites.net/api/HttpTriggerJS1?code=eDdsVVEUvnH4o/BPPxNhFJgv3A/J5J6zhm66c1yLvnUzcvnLCS3I0Q=="
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
