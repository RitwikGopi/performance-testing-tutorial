from string import ascii_letters

from locust import HttpUser, between, stats, task

stats.PERCENTILES_TO_CHART = [0.5, 0.9]


def generate_string():
    letters = list(ascii_letters)
    non_repeating = letters.pop()
    new_string = []
    for letter in letters:
        new_string.extend(list(letter * 100))
        # for _ in range(10000):
        #     new_string.append(letter)
    new_string.append(non_repeating)
    return "".join(new_string)


SEARCH_STRING = generate_string()
print(len(SEARCH_STRING))


class ApiUser(HttpUser):
    host = "http://0.0.0.0:5000"
    wait_time = between(0.1, 0.3)  # wait time between requests

    @task
    def perform_search(self):
        url = "/search"
        resp = self.client.post(url, data=SEARCH_STRING)
