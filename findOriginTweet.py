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


CONSUMER_KEY = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

dbName = ''

streamListener = StreamListener()
auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)
stream = tw.Stream(auth, streamListener)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
tweet = api.get_status(sys.argv[1])
tweet_js = json.dumps(tweet._json)
y = json.loads(tweet_js)
jsonTweetFile=open(dbName+'/tweets/'+y['id_str']+'.json','w')
json.dump(y,jsonTweetFile)






