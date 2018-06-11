# Load Testing 
This contains directory contains the file needed to load test each platform and the results of each test.

## Setting up Locust
You will need to edit the hardcoded values of the URL to invoke the lambda and the argument being passed, depending on what you want to test

## Running Locust
* First, make sure you have Locust 0.8 installed.
* Simply run ```locust``` in the directory with locustfile.py
* Using a web browser, open 127.0.0.1:8087 
* Input your desired maximum amount of users and spawn rate
* After your desired amount of time use the web interface to download the data
