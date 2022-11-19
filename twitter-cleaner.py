import tweepy
import config

bearer_token = config.bearer_token
api_key = config.api_key
api_secret = config.api_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

username = "yourusername"
maxresults = 5

def main():
    
    client = tweepy.Client(bearer_token)

    # Verify auth
    response = client.get_user(id=None, username=username)
    user_id = response.data.id

    # Search Recent Tweets
    response = client.get_users_tweets(id=user_id, max_results=maxresults)
    # The method returns a Response object, a named tuple with data, includes,
    # errors, and meta fields
    if response.meta["result_count"] == 0:
        print("No recent tweets")
        exit(0)

    # In this case, the data field of the Response returned is a list of Tweet
    # objects
    tweets = response.data

    # By default, this endpoint/method returns 10 results
    # You can retrieve up to 100 Tweets by specifying max_results

    superclient = tweepy.Client(
                            consumer_key=api_key,
                            consumer_secret=api_secret,
                            access_token=access_token,
                            access_token_secret=access_token_secret
    )

    for tweet in tweets:
        print(tweet.id)
        print(tweet.text)
        superclient.delete_tweet(id = tweet.id)

if __name__ == "__main__":
    main()
