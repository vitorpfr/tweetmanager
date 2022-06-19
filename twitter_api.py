import requests
from requests.structures import CaseInsensitiveDict
import yaml

config = yaml.safe_load(open("config.yml"))

credentials = config["credentials"]
api_key = credentials["api_key"]
api_key_secret = credentials["api_key_secret"]
token = credentials["token"]

twitter_api = "https://api.twitter.com"


def request(url_suffix):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    r = requests.get(f"{twitter_api}{url_suffix}", headers=headers)

    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Request to Twitter API failed: ", r.status_code, " ", r.reason)
