import twitter_api
import json


def pprint(content):
    print(json.dumps(content, indent=4))


def get_tweet_id(tweet):
    tweet.get("id")


def get_user_by_username(username):
    return twitter_api.request(f"/2/users/by/username/{username}")


# TODO: finish implementation of this function - it should return a list of all tweet ids between start time and end time
# TODO: add logger library
def get_list_of_tweets_between_date(user_id):
    page = 1
    extract_results_from_all_pages = False

    start_time = "2010-12-10T16:45:52.000Z"
    end_time = "2020-12-10T16:45:54.000Z"
    max_results = 100  # max value accepted is 100
    tweet_fields = "created_at"

    url = f"/2/users/{user_id}/tweets" \
          f"?max_results={max_results}" \
          f"&tweet.fields={tweet_fields}" \
          f"&start_time={start_time}" \
          f"&end_time={end_time}"

    response = twitter_api.request(url)
    tweets = list(
        map(get_tweet_id, response.get("data"))
    )

    pprint(response)
    print(f"first response has {len(response.get('data'))} tweets")

    if extract_results_from_all_pages:
        while "next_token" in response.get("meta"):
            next_token = response.get("meta").get("next_token")
            response = twitter_api.request(url + f"&pagination_token={next_token}")

            tweets = tweets + list(map(get_tweet_id, response.get("data")))
            page += 1

    print(f"total of {page} pages searched")
    return tweets

# TODO: start deleting tweets according to rate limit, marking them as deleted in the database to guarantee idempotency

# TODO: write tests
