#!/usr/bin/env python
import getpass

from FileEncryptor import decryptWithPassword,kdf,encryptWithHash

class Authenticator:
	"""
	"""
	def __init__(self):
		self.__plaintext = None
		self.__ciphertext = None
		self.__hash = None
		self.__salt = None
		self.__filename = None

	
	def EncryptFile(self,plaintext):
		self.__ciphertext = encryptWithHash(plaintext,self.__hash,self.__salt)

	
	def DecryptFile(self,password):
		self.__plaintext = decryptWithPassword(
			self.__ciphertext,
			password=password,
			)

		if self.__plaintext is None:
			return False
		
		#print(self.__plaintext.decode())
		self.__salt = self.__ciphertext[-16:]
		self.__hash = kdf(password,self.__salt)		
		return True
	

	def Authenticate(self,filename):
		"""
		Authenticates user if they can decrypt password file with integrity,
		interactions with user done through TERMINAL

		Parameters:
		filename (str): path to file of encrypted passwords

		Returns
		Bool: True if user was Authenticated

		"""
		# try:
		self.__filename = filename
		reader = open(filename,"rb")
		self.__ciphertext = reader.read()
		reader.close()

		userAttempts = 3
		while(userAttempts > 0):
			userAttempts -= 1

			password = getpass.getpass(" UNLOCK: ")
			if self.DecryptFile(password) == True:
				return True
			else:
				print("\n" + 
					" Incorrect password \n " +
					str(userAttempts) + " attmpts left")
		return False
		# except:
		# 	e = sys.exc_info()[0]
		# 	print(" Error: %s" % e)
		# 	return False
	
	def Close(self,plaintext):
		"""
		Write changes to file then close

		Parameters:
		plaintext: updated plaintext to save to file

		Returns:
		Bool: True if it completes writing to file
		"""
		# try:
		self.EncryptFile(plaintext)
		
		writer = open(self.__filename,"wb")
		writer.write(self.__ciphertext)
		writer.close()
		return True
		# except:
		# 	return False

	def GetFile(self):
		"""
		Getter Function to get decrypted file content

		Returns:
		String: plaintext with encrypted passwords
		"""
		return self.__plaintext.decode()

	def GetHash(self):
		"""
		Getter Function to get passwords hash

		Returns:
		Bytes: Hash of password 
		"""
		return self.__hash
