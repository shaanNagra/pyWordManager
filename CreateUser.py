#!/usr/bin/env python
import getpass
import argon2

from passwordValidation import Validate
from FileEncryptor import encryptWithPassword

templateJson = '{}'

def createUser(filename):
	"""
	
	"""
	try:
		
		print(" creating password safe")
		print(" please provide master password\n")
		
		userAttempts = 3
		hasher = argon2.PasswordHasher()
		while(userAttempts > 0):
			
			userAttempts -= 1

			#type password to set masterpassword
			password = getpass.getpass(" master password: ")
			#pass validations
			if Validate(password) == True:			
				#retype the same password
				retyped = getpass.getpass(" retype master password: ")		
				if password == retyped:
					
					#set masterpassword
					
					userAttempts = 0
					cyphertext = encryptWithPassword(templateJson,password)
					
					if cyphertext != None:
						f = open(filename,"wb")
						f.write(cyphertext)
						f.close()
						print(" password safe created 🔒 \n")
						return True
					else:
						print(" could not create password safe")
						return False
				
				else:
					print("\n" + 
						" passwords didnt match")
			print(" " + str(userAttempts) + " attmpts left")	
		return False
	except:
		print("exception caught")
		return False
