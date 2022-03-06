from os import access
import tweepy
import time
from dotenv import load_dotenv

load_dotenv()

consumer_key = API_KEY = os.environ.get('API_KEY')
consumer_secret = API_KEY_SECRET = os.environ.get('API_KEY_SECRET')
access_token = ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
access_token_secret = ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)


def get_tweets(user_id: int):
    tweets = client.get_users_tweets(
        id=user_id, max_results=10, tweet_fields=["text"], user_auth=True)

    return [tweet for tweet in tweets.data]


# get to print each line in bot_ids-twitter.txt
# once you can do that, change operation to get_tweets
# in separate file, get working list export to file
# once you have that, apply it to these lists
start = time.time()

user_tweets = []

with open("user_ids-twitter.txt", "r") as bot_id_file:
    for j in range(0, 10):
        line = bot_id_file.readline()
        if line:
            print("---", line)
            user_tweets.extend(get_tweets(int(line)))

with open("user_tweets-twitter.txt", "w") as bot_tweets_file:
    for i in len(user_tweets):
        print(i)
        for j in 10:
            print(user_tweets[i][j])
            # bot_tweets_file.write(user_tweets[i][j])

end = time.time()

time.sleep(900 - start - end)