from cryptography.fernet import Fernet
#keyGenerator = Fernet.generate_key()
#print keyGenerator
key = "MSwMGl8kJZfj5_zLfpfeM9fE9Y-_TqsdHGl38AhnMvk="
#print "Key "+ key
f = Fernet(key)


def encode(message):
	#f = Fernet(key)
	token = f.encrypt(message)
	#print token
	return token
	


def decode(message):
	#f = Fernet(key)
	#token = f.decrypt(message)
	#print token
	#return token
	return f.decrypt(message)
	
#print "Encryption: " 
#mesg = encode("Hello!")
#print '\n'
#print "Decryption: " 
#decode(mesg)







	
