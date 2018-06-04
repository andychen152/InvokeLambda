# simply run "$ locust"

from locust import HttpLocust, TaskSet, task
import json

class UserBehavior(TaskSet):
    def on_start(self):
        self.arg = json.dumps({"num":1000000})
        self.head = {'Content-Type': 'application/json'}
        # pass

    def on_stop(self):
        pass

    @task(1)
    def profile(self):
        self.client.post("/api/HttpTriggerJS1?code=dop/aTm6SCDIyAaudKn25mY85pczrZOft630FOFu4uzxPBxiuIGkxw==", headers=self.head, data=self.arg)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "https://computepi.azurewebsites.net"


    # automatically waits 1 second if nothing is specified
    # min_wait = 5000
    # max_wait = 9000
