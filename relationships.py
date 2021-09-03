import shutil
import sys
import os
import networkx as nx 
import tweepy as tw
import glob
import pathlib
import matplotlib.pyplot as plt
import time
from tweepy import OAuthHandler

db_name = sys.argv[1]
path = '/tweets/'

#request Twitter for the following keys
CONSUMER_KEY = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

nodes=[]
edges = []

for file in glob.glob(os.path.join(path, '*.txt')):
    f = open(file, 'r')
    inFile = open('C:/Users/kmpou/OneDrive/Desktop/datasets/'+db_name+'/edges/'+os.path.basename(file),'w+')
    nodes=[]    
    edges = []
    root = str(f.readline().split('\t')[0]) #root user who created tweet
    print('ROOT NODE:', root)
    nodes.append(root)
    for line in f:
        print(line)
        user1,user2,timestamp = line.split('\t')  #user1 -> user2
        if user1 != root:
            edges.append(tuple([user2,user1]))
            nodes.append(user1)
            inFile.write(user1+'\t'+user2+'\n') 
        else:
            for i in nodes[::-1]:
                try:
                    status = api.show_friendship(source_id=user2,target_id=i) #user2 follows i
                    if status[0].following == True:
                        edges.append(tuple([i,user2]))
                        inFile.write(i+'\t'+user2+'\n') 
                        nodes.append(user2)
                        print(user2+' FOLLOWS '+i+' : '+str(status[0].following))
                        break
                except Exception as e:
                        print(e)
                        if str(e) == "[{'code': 63, 'message': 'User has been suspended.'}]" or str(e) == "[{'code': 50, 'message': 'User not found.'}]":
                            print('ROOT USER HAS BEEN SUSPENDED OR NOT FOUND!')
                        elif str(e) == "[{'code': 163, 'message': Could not determine source user.}]":
                            print('COULD NOT DETERMINE SOURCE USER!')
    f.close()
    inFile.close()
        
