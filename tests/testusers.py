import requests
from pprint import pprint
def test_create():
    sample = {"name": "duane", "hobby": "games", "sex": "male"}
    resp = requests.post("http://127.0.0.1:5000/user", json=sample)
    pprint(resp.json())

if __name__ == "__main__":
    test_create()