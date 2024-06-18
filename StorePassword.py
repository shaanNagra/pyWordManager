#!/usr/bin/env python
import getpass
import json

from CreatePassword import createPassword
from passwordValidation import Validate
from passwordEncryption import encrptPassword
from Authenticator import Authenticator

class StorePassword:
	def __init__(self):
		self.__authenticator = Authenticator()
		self.__database = None


	def Storepassword(self,filename):

		if self.__authenticator.Authenticate(filename) == True:
			print(" ✅ Authenticated ")
		else:
			return
		
		self.__database = json.loads(self.__authenticator.GetFile())

		password = None
		id = None

		while(True):
			userIdInput = input(" What is the password for? ")
			
			if userIdInput == "exit":
				return None

			if self.__existsInFile(userIdInput) == True:
				print(" password for "+userIdInput+" exists")
				userInput = input("  do you want to overide? [y/n]\n ").lower().strip(" ")
				if userInput == "yes" or userInput == "y":
					id = userIdInput
					break
				elif userInput == "no" or userInput == "n":
					print()
			else:
				print(" ID = "+userIdInput)
				id = userIdInput
				break
		
		while(True):
			userInput = input(" Do you want to generate password? [y/n]\n ").lower().strip(" ")	
			
			if userInput == "yes" or userInput == "y":
				userInput = input(" password length: ")
				if userInput.isnumeric:
					if int(userInput) >= 8 and int(userInput) <= 80:
						password = createPassword(int(userInput))
						break
					else:
						print()
				else:
					print()

			elif userInput == "no" or userInput == "n":
				
				while(True):
					userInput = getpass.getpass(" password: ")
					if Validate(userInput) == True:
						password = userInput
						break

					print("retry ")

			elif userInput == "exit":
				return None
		
			if password is not None:
				break

		fileContent = self.__setPassword(id,password)
		if fileContent is not None:
			self.__authenticator.Close(fileContent)
			print("password saved")




	def __existsInFile(self,userInput):
		if userInput in self.__database:
			return True
		return False


	def __setPassword(self,id,password):
		key = self.__authenticator.GetHash()
		encryptedpassword = encrptPassword(password,key)

		if encryptedpassword is not None:
			self.__database[id] = bytes.hex(encryptedpassword)
			return json.dumps(self.__database)
		return None
