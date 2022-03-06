import json
import os
from dotenv import load_dotenv
import tweepy
load_dotenv()

consumer_key = API_KEY = os.environ.get('API_KEY')
consumer_secret = API_KEY_SECRET = os.environ.get('API_KEY_SECRET')
access_token = ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
access_token_secret = ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)
  
# using get_user with id
_id = "103770785"
user = api.get_user(_id)
  
# printing the name of the user
print("The id " + _id +
      " corresponds to the user with the name : " +
      user.name)