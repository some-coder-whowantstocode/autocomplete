from locust import HttpUser, task, between
import random

class AutocompleteUser(HttpUser):
    wait_time = between(0.5, 2)

    @task
    def addword(self):
        query = random.choice(["a", "ap", "app", "appl", "apple", "b", "ban", "banana"])
        response = self.client.post("/addWord", json={"word": query})
        print(response.text)

    @task
    def completeword(self):
        query = random.choice(["a","b"])
        response = self.client.post("/completeWord", json={"word": query})
        print(response.text)