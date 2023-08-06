import json
from config import config
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML

def bottom_toolbar():
    return HTML('Press <b><style bg="ansired">ESC + ENTER</style> to submit</b>!')

def send_tweet(client, tweet):
    res = client.create_tweet(text=tweet, user_auth=True)
    _dict = json.loads(res.text)
    _id = _dict["data"]["id"]
    print(f"\nYour tweet {_id} has been sent!")

def get_tweet(toolbar):
    print("+-+-+")
    tweet = prompt(multiline=True, bottom_toolbar=toolbar)
    print("+-+-+")
    return tweet

def create():
    """Creat a new tweet in the interactive mode"""
    tweet = get_tweet(bottom_toolbar)
    client = config()
    send_tweet(client, tweet)