import os, sys
import time
import datetime

import simplejson

import twitter

api = twitter.Api(consumer_key='Insert your key here',
                       consumer_secret='Insert your key here',
                       access_token_key='Insert your key here',
                       access_token_secret='Insert your key here',
                       debugHTTP=True)



since_id = None
person = raw_input('Enter Twitter User Name: ')

try:
     print '-+'*10, 'User Timeline'
     for status in api.GetUserTimeline(screen_name=person, count=200,exclude_replies=True):
         item = status.AsDict()
         

         w=  item['created_at'] + ' :: ' + item['text']
         
         

         saveFile = open('tweets.csv', 'a') 
         saveFile.write(w.encode('utf-8'))
         saveFile.write('\n')
         saveFile.close()

         #print w  
          


finally:
     print '*'*50

