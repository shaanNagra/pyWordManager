#!/usr/bin/env python
import re

def Validate(password):
	flag = True
	output = " ------------- \n password must contain:"
	if len(password) < 8:
		output += "\n   * be atleast 8 characters long"
		flag = False
	if not re.search("[a-z]",password):
		output += "\n   * atleast one lowercase character"
		flag = False
	if not re.search("[A-Z]",password):
		output += "\n   * atleast one uppercase character"
		flag = False
	if not re.search("[0-9]",password):
		output += "\n   * atleast one number character"
		flag = False
	
	if flag == False:
		print(output+"\n")
	
	return flag
	