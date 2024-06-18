#!/usr/bin/env python
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import sys

def decryptPassword(text,key):
		try:
			ciphertext = text[:-32]
			iv = text[-32:-16]
			tag = text[-16:]

			decryptor = Cipher(
				algorithm=algorithms.AES(key),
				mode=modes.GCM(iv,tag),
				backend=backends.default_backend(),
			).decryptor()	
			
			plaintext = decryptor.update(ciphertext) + decryptor.finalize()
			
			return plaintext
		except:
			return None

def encrptPassword(plaintext,key):
	try:
		iv = os.urandom(16)

		encryptor = Cipher(
			algorithm=algorithms.AES(key),
			mode=modes.GCM(iv),
			backend=backends.default_backend(),
			).encryptor()

		cyphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
		cyphertext = cyphertext + iv + encryptor.tag

		return cyphertext
	except:
		e = sys.exc_info()[0]
		print(" Error: %s" % e)
		# return None
