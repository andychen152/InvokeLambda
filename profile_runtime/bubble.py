import requests
import json


def CreateInput():
	ret = [0 for _ in xrange(4)]
	for i in xrange(1, 5):
		json_str = requests.get("http://www.cs.ucsb.edu/~andrewhuang/" + str(i) + ".json").text
		json_dict = json.loads(json_str)

		ret[i-1] = json.dumps(json_dict)
	return ret


NUM_TESTS = 1
inputs = CreateInput()

URLS = {
	"GCP": "https://us-central1-bold-script-204219.cloudfunctions.net/bubblesort",
	"AWS": "https://ajkxgtlsxf.execute-api.us-west-1.amazonaws.com/prod/bubble",
	"Azure": "https://bubblesort.azurewebsites.net/api/HttpTriggerJS1?code=aK10F4d7Jb/IH94tOdNJy0oP0sOjr9jpSnGPepzjH2dCyrutMmmQog=="
}

avgs = {
	"GCP": [0.0]*4,
	"AWS": [0.0]*4,
	"Azure": [0.0]*4
}

for i, put in enumerate(inputs):
	for _ in xrange(NUM_TESTS):
		for platform in URLS:
			val = 0
			headers = {'Content-Type': 'application/json'}
			r = requests.post(URLS[platform], headers=headers, data=put)
			if platform == "GCP":
				val = int(r.text)
			else: #platform in ["AWS", "Azure"]:
				val = int(r.text[1:-1])

			avgs[platform][i] += val

for platform in avgs:
	print platform
	for i, val in enumerate(avgs[platform]):
		print "test:", i, ":", val/NUM_TESTS
