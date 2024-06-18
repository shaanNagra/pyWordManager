#!/usr/bin/env python

import os
import getpass
import pyfiglet


from CreateUser import createUser
from GetPassword import GetPassword
from StorePassword import StorePassword

def App():
	try:
		user = getpass.getuser()
		filename = user+"Passwords.txt"

		header = pyfiglet.figlet_format(" Password  Safe",font='slant')
		print(header)


		if not os.path.exists(filename):
			print(" "+user+" does not have a password file...")
			userSet = createUser(filename)

			if userSet == False:
				print(" Exiting...")
				exit()

		while(True):
			userinput = input(" Do you want to add or view a password? [add/view/exit] \n  ")
			
			if userinput == "add":
				print()
				sp = StorePassword()
				sp.Storepassword(filename)
				exit()
			elif userinput == "view":
				gp = GetPassword()
				gp.Getpassword(filename)
				exit()
			elif userinput == "exit":
				exit()
			else:
				print(" invalid input \n valid inputs: store, view, exit")
	except:
		exit()

#run script
App()
