#!/usr/bin/env python

import json
import re

from passwordEncryption import decryptPassword
from Authenticator import Authenticator

class GetPassword:
	"""
	"""
	def __init__(self):
		self.__authenticator = Authenticator()
		self.__fileContent = None	
		self.__database = None


	def Getpassword(self,filename):
		"""
		module authenticates user and allows access to saved passwords
		interactions done through TERMINAL

		Parameters:
		filename (str): path to encrypted passwrods

		returns: 
		nothing
		"""
		if self.__authenticator.Authenticate(filename) == True:
			print(" ✅ Authenticated ")
		else:
			return
		
		self.__database = json.loads(self.__authenticator.GetFile())
		
		print(" please provide:\n  * cmd 'get' followed by id\n  * cmd 'list' to see all matching id's \n  * cmd 'exit' to exit")
		while(True):
			userinput = input(" cmd: ")
			userinput = userinput.lower().split(" ")
			
			if userinput[0] == "get" and len(userinput) >=2:
				if self.__existsInFile(userinput[1]):
					self.__getPassword(userinput[1])
					exit()
				else:
					print("  '" + userinput[1] + "' Not in database")
			
			elif userinput[0] == "list":
				searchString = ""
				if len(userinput) >= 2:
					searchString = userinput[1]

				self.__Listall(searchString)

			elif userinput[0] == "exit":
				return
			else:
				print(" please provide:\n  * cmd 'get' followed by id\n  * cmd 'list' to see all matching id's \n  * cmd 'exit' to exit")
				

	def __Listall(self,searchString):
		"""
		prints id's in database that match searchString

		Parameters:
		searchString (string):  string to look for in database

		returns: 
		Nothing
		"""
		for id in self.__database:
			if re.search(searchString, id):
				print("  > "+str(id))


	def __existsInFile(self,userInput):
		"""
		check if 'id' is in database

		Parameters:
		userInput (string):  id in database

		returns: 
		Bool:   True if found
		"""
		if userInput in self.__database:
			return True
		return False


	def __getPassword(self,id):
		"""
		get password from database

		Parameters:
		id (string):   id in database

		returns: 
		Nothing
		"""
		password = bytes.fromhex(self.__database[id])
		password = decryptPassword(
			password,
			self.__authenticator.GetHash(),
			)
		print("  \n  password for "+ id +" : "+password.decode())
		return