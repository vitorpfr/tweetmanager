import requests
from requests.structures import CaseInsensitiveDict
import yaml

# constants
config = yaml.safe_load(open("config.yml"))

credentials = config["credentials"]
api_key = credentials["api_key"]
api_key_secret = credentials["api_key_secret"]
token = credentials["token"]

twitter_api = "https://api.twitter.com"


# helper functions
def get_user_by_username(username):
    url = f"{twitter_api}/2/users/by/username/{username}"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r.text
    else:
        raise Exception("Request to Twitter API failed: ", r.status_code, " ", r.reason)

# TODO: get list of tweets to be deleted, provided a user id

# TODO: start deleting tweets according to rate limit, marking them as deleted in the database to guarantee idempotency

# TODO: write tests