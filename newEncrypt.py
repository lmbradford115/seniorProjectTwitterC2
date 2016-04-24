#Both attacker and enemy computer need this 

#Documentation: https://cryptography.io/en/latest/fernet/

#Symmetric encryption 
from cryptography.fernet import Fernet

#Call this commented out method below the generate new key
#keyGenerator = Fernet.generate_key()
#print keyGenerator
key = "MSwMGl8kJZfj5_zLfpfeM9fE9Y-_TqsdHGl38AhnMvk="
#print "Key "+ key

f = Fernet(key)


def encode(message):
	token = f.encrypt(message)
	return token
	


def decode(message):
	return f.decrypt(message)
	
