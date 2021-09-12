import os
import sys
import json
import requests
import os.path

import tweepy as tw
import datetime
import time
import calendar

from datetime import datetime
from time import strptime
from tweepy import OAuthHandler, Stream, StreamListener
from urllib3.exceptions import ProtocolError
from operator import itemgetter
from requests_oauthlib import OAuth1
from os import path

===============================================================
request Twitter for the following keys
CONSUMER_KEY = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
===============================================================

if not os.path.exists(' /tweets/'):               
    os.mkdir(' /tweets/')
if not os.path.exists(' /retweets/'):                  
    os.mkdir(' /retweets/')
if not os.path.exists(' /replies/'):                 
    os.mkdir(' /replies/')
if not os.path.exists(' /quotes/'):                 
    os.mkdir(' /quotes/')

class StreamListener(tw.StreamListener):
    def on_data(self, data):
        story = json.loads(data)
        for keyword in searchTerms:
            if keyword in story['text']:
                #quote
                ===============================================================
                if story['is_quote_status'] == True or story['id_str'] == ID:
                    jsonQuoteFile=open('quotes/'+story['id_str']+'.json','w')
                    json.dump(story,jsonQuoteFile)
                #retweet
                ===============================================================
                elif 'retweeted_status' in story or story['retweeted_status']['id_str'] == ID:
                    jsonRetweetFile=open('retweets/'+story['id_str']+'.json','w')
                    json.dump(story,jsonRetweetFile)
                #reply
                ===============================================================
                elif story['in_reply_to_status_id'] is not None or story['in_reply_to_status_id_str'] == ID:
                    jsonReplyFile=open(replies/'+story['id_str']+'.json','w')
                    json.dump(story,jsonReplyFile)
                #tweet
                ===============================================================
                else:
                    jsonTweetFile=open('tweets/'+story['id_str']+'.json','w')
                    json.dump(story,jsonTweetFile)        

    def on_error(self, status):
        print(status)
        
    
if __name__ == '__main__':   
    while True:
        try:
            story ={}
            if (len(sys.argv) == 2):
                searchTerms = sys.argv[1].split(';')     #command line argument for keywords separated with semicolon  --input: "keyword1;keyword2"--
            else:
                print("No parameters supplied. Exiting...")
                sys.exit(0)

            streamListener = StreamListener()
            auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
            auth.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)
            stream = tw.Stream(auth, streamListener)
            stream.filter(track=searchTerms, stall_warnings=True)
        except Exception as error:
            api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            continue
        except StopIteration:
            break
        


        
   
