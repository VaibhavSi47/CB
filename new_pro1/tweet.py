import tweepy
import pandas as pd

consumer_key = "NibdqaCreleom5UW64FcWTOj2"
consumer_secret = "CBamSqcqX7U13A0UPmuKuGXMBkOIAX7yHlMR6LjSRQHbWfx4nc"
access_token = "1393060774529040388-Nt0cRn2pE1lSW5XgXRXyGhBuELXpmB"
access_token_secret = "CqhTiM7c4CSsT5VA8OWamcPwlzyuoneXmgzV1cqdfKRpu"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

cursor = tweepy.Cursor(api.user_timeline, id="COVIDNewsByMIB", tweet_mode="extended").items(20)

for i in cursor:
    #    print(dir(i))
    print(i.full_text, i.created_at)
    print("\n")

cursor = tweepy.Cursor(api.search, q="माझी Mumbai, आपली BMC", tweet_mode="extended").items(20)

for i in cursor:
#    print(dir(i))
    print(i.full_text, i.created_at, i.source)
    print("\n")

cursor = tweepy.Cursor(api.user_timeline, id="PanvelCorp", tweet_mode="extended").items(20)

for i in cursor:
#    print(dir(i))
    print(i.full_text, i.created_at, i.source)
    print("\n")

cursor = tweepy.Cursor(api.search, q="IndiaFightsCOVID19", tweet_mode="extended").items(20)

for i in cursor:
#    print(dir(i))
    print(i.full_text, i.created_at, i.source)
    print("\n")