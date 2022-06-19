import delete


if __name__ == '__main__':
    user = "vitorpfr"
    user_id = delete.get_user_by_username(user).get("data").get("id")
    print(f"user_id = {user_id}")

    tweets = delete.get_list_of_tweets_between_date(user_id)
    print(tweets)
