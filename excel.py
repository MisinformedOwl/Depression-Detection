from openpyxl import Workbook
import datetime as dt
import tweepy
import numpy
from time import sleep
from tqdm import tqdm

consumer_key = '8ZgghcwUoDm6gY8YYtlDSrzjH'
consumer_secret = 'RLSdYYGduGokDJ4nsKmhmumEpF99NNoqaQOrcLsxdCBWgYKk3k'
access_token_key = '1156170455147057152-6AC3AjpyEM1ixgRRulp04HrU04hU8L'
access_token_secret = 'jZLCfV7uQKeRU5CcHOgiFba26vF3Mm2Pxtx1RoznHa6rC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Phrases"
sheet["B1"] = "Depressed"


def TweetCollection(thread, label):
    global index
    results = api.search(q=f"#{thread} -filter:retweets", count=1000, tweet_mode="extended", include_rts = False, lang="en")
    
    for tweet in results:
        sheet[f"A{index}"] = tweet.full_text
        sheet[f"B{index}"] = label
        index = index + 1
        
threads = [("depressed",1), ("happy",0), ("sad",1), ("joyful",0)]

index = 2
for thread, label in threads:
    TweetCollection(thread, label)
    
while True:
    try:
        workbook.save(filename="data/man.xlsx")
        break
    except:
        print("Currently busy trying again...")
        sleep(5)