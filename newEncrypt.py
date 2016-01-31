from cryptography.fernet import Fernet
#key = Fernet.generate_key()
key = "nCMgwxYNuBL-UfSkYHsP0z6heL4z2zATKC7OaiZuowY="
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

	
