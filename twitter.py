import tweepy

ACCESS_KEY = 'test_access_kEy'
ACCESS_SECRET = 'test_access_secRET'
CONSUMER_KEY = 'test_consumer_KEy'
CONSUMER_SECRET = 'tEST_Consumer_secret'
file = ''
client = tweepy.Client(access_token=ACCESS_KEY,
                    access_token_secret=ACCESS_SECRET,
                    consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET)

client.create_tweet(text='urmom',media_ids=file)