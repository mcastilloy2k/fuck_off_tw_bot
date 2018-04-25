#!/usr/bin/env python
import random
from Services.readfile import read_file
from Services.printer import print_json
from twython import Twython

# Credentials setup
# Loads in 'twitter-creds.json' values as a dictionary
credentials = read_file("twitter-creds.json")

# Sets config values from the config file
CONSUMER_KEY = credentials["consumer_key"]
CONSUMER_SECRET = credentials["consumer_secret"]
ACCESS_TOKEN_KEY = credentials["access_token_key"]
ACCESS_TOKEN_SECRET = credentials["access_token_secret"]

# Create the Twython Twitter client using our credentials
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

# User IDs
USER_IDS = {225664792}
MY_ID = 35412629
# Todo Add this list from a database or any configuration file

# Sample random tweets
potential_tweets = [
    'Holis',
    'Holis x2',
    'Testan'
]


def send_tweet(tweet_text):
    """Sends a tweet to Twitter"""
    twitter.update_status(status=tweet_text)


def is_valid_user():
    """Validates the credentials"""
    user = twitter.verify_credentials()
    return user['id'] > 0


def get_mentions_from_users():
    """Get user notifications"""
    user_mentions = twitter.get_mentions_timeline()
    return [x for x in user_mentions if x['user']['id'] in USER_IDS]


def get_user_timeline():
    tweets = []
    for user_id in USER_IDS:
        tweets = twitter.get_user_timeline(user_id=user_id,
                                           max_id=None,
                                           count=10,
                                           trim_user=True,
                                           exclude_replies=True,
                                           include_rts=False) + tweets
    tweets = [x for x in tweets if 'quoted_status' in x and x['quoted_status']['user']['id'] == MY_ID]
    for tweet in tweets:
        print_json(tweet)


def handler(event, context):
    """Sends random tweet from list of potential tweets"""
    send_tweet(random.choice(potential_tweets))


if __name__ == "__main__":
    is_valid = is_valid_user()
    if not is_valid:
        print('Credentials are not valid, please check the twitter-creds.json')
        exit()
    # mentions = get_mentions_from_users()
    # print(mentions)
    get_user_timeline()
