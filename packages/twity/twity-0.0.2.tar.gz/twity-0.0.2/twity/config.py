import os
import tweepy
import requests
from dotenv import load_dotenv

def config():
    load_dotenv()
    client:tweepy.Client

    try:
        client = tweepy.Client(
            bearer_token=os.environ["BEARER_TOKEN"],
            consumer_key=os.environ["API_KEY"],
            consumer_secret=os.environ["API_KEY_SECRET"],
            access_token=os.environ["ACCESS_TOKEN"],
            access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
            return_type= requests.Response,
            wait_on_rate_limit=True
        )   
    except Exception as e:
        print("An error occured: ",e)

    return client
    