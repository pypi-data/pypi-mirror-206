from config import config

def store_variables(bearer_token, api_key, api_key_secret, access_token, access_token_secret):
    with open(".env", "w") as file:
            file.writelines([
                f"BEARER_TOKEN={bearer_token}\n",
                f"API_KEY={api_key}\n",
                f"API_KEY_SECRET={api_key_secret}\n",
                f"ACCESS_TOKEN={access_token}\n",
                f"ACCESS_TOKEN_SECRET={access_token_secret}"
            ])
    print("Authentification details has been stored!")

def auth(bearer_token, api_key, api_key_secret, access_token, access_token_secret):
    """Authenticate the twitter user"""
    store_variables(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
    config()
    print("Your authentification is successfull!") 
