import tweepy
from newEncrypt import *
#import sys  
#reload(sys)  
#sys.setdefaultencoding('utf-8')

consumer_key = 'zLZ2NN1qemQChgVOae3QlgNtp'
consumer_secret = 'hbAZzMFdpff1sDHp50d4qt4l7QumyUfhxSybl5Smne1eTi2mEw'
access_token = '4827323871-Oig9GWZc6gkVUYK7oTkQO1O4dmoJLuCaY8vE6Dh'
access_token_secret = 'h2BMjDxt24XolArqy2vuRJYauMqKp2boNIgWUdHwlmGxD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	test = str(tweet.text)
	bytes = str.encode(test)
	type(bytes)	
	print "Decoded message: " + decode(bytes)
	#api.destroy_status(tweet.id)
   		
