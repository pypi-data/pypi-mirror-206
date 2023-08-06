from config import config

def delete(id):
    """Delete a recent tweet"""
    client = config()
    client.delete_tweet(id, user_auth=True)
    print(f"Tweet {id} has been deleted!")
