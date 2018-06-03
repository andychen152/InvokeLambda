# simply run "$ locust"

from locust import HttpLocust, TaskSet, task
import json

class UserBehavior(TaskSet):
    def on_start(self):
        self.arg = json.dumps({"iter":10000000})
        self.head = {'Content-Type': 'application/json'}
        # pass

    def on_stop(self):
        pass

    @task(1)
    def profile(self):
        self.client.post("/calculate_pi", headers=self.head, data=self.arg)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "https://us-central1-bold-script-204219.cloudfunctions.net/"

    # automatically waits 1 second if nothing is specified
    # min_wait = 5000
    # max_wait = 9000
