from openpyxl import Workbook
import tweepy
from time import sleep
from tqdm import tqdm
import keyboard

#Keys for accessing twitter API
consumer_key = '8ZgghcwUoDm6gY8YYtlDSrzjH'
consumer_secret = 'RLSdYYGduGokDJ4nsKmhmumEpF99NNoqaQOrcLsxdCBWgYKk3k'
access_token_key = '1156170455147057152-6AC3AjpyEM1ixgRRulp04HrU04hU8L'
access_token_secret = 'jZLCfV7uQKeRU5CcHOgiFba26vF3Mm2Pxtx1RoznHa6rC'

#Access and prepare api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

#Open library for working in excel sheets
workbook = Workbook()
sheet = workbook.active

#Assign the labels for each piece of data
sheet["A1"] = "Phrases"
sheet["B1"] = "Depressed"

#Function for saving the excel file
def savebook(workbook):
    while True:
        try:
            workbook.save(filename="data/man.xlsx")
            break
        except:
            print("Currently busy trying again...")
            sleep(5)

#This function goes through all of the twitter hashtags i wish to search through
def TweetCollection(thread, labeled):
    #Global index so it continues through all cells in the excel file
    global index
    results = api.search(q=f"#{thread} -filter:retweets", count=100, tweet_mode="extended", include_rts = False, lang="en")
    
    #For all tweets collected...
    for tweet in results:
        #If the label passed is 2, manually label tweets in this catagory
        if labeled == 2:
            print()
            print(index, "-----------------------------------------------------------")
            print()
            print(tweet.full_text)
            key = keyboard.read_key()
            sleep(0.2)
            #Label as depressed
            if key == "1":
                label = 1
                #Skip data
            elif key == "#":
                continue
            #Save and exit
            elif key == '/':
                savebook()
            #Else it is not depressed
            else:
                label = 0
            sheet[f"B{index}"] = label
        #Else use the label passed either 0 or 1
        else:
            sheet[f"B{index}"] = labeled
        sheet[f"A{index}"] = tweet.full_text
        index = index + 1
            
#A tuple containing all #'s i wish to search aswell as their associated labels
threads = [("depressed",1), ("happy",0), ("sad",1), ("joyful",0)]
#Start index at 2 since the first row is assigned to catagory names
index = 2
#Going through all these threads collect tweets
for thread, label in threads:
    TweetCollection(thread, label)
    
#Save workbook and end.
savebook(workbook)