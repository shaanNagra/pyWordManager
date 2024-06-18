#!/usr/bin/env python
__author__ = "shaan nagra"

import secrets
import string


def createPassword(length):
	'''
	'''
	if length >= 8 and length <=80:
		password = ''
		for x in range(length):
			password += secrets.choice( 
				string.ascii_letters +
				string.digits +
				string.punctuation 
				)
		return password
	else:
		print("password length must be between 8 and 80")
		return 