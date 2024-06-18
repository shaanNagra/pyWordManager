#!/usr/bin/env python
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import argon2
import os

def __decrypt(text,password=None,key=None):
		try:
			ciphertext = text[:-48]
			iv = text[-48:-32]
			tag = text[-32:-16]
			salt = text[-16:]

			if key == None:
				key = kdf(password,salt)

			decryptor = Cipher(
				algorithm=algorithms.AES(key),
				mode=modes.GCM(iv,tag),
				backend=backends.default_backend(),
			).decryptor()	
			
			plaintext = decryptor.update(ciphertext) + decryptor.finalize()
			
			return plaintext
		except:
			return None

def decryptWithPassword(text,password):
	return __decrypt(text,password=password)

def __encrpt(plaintext,password=None,key=None,salt=None):
	try:
		iv = os.urandom(16)

		if key == None:
			salt = os.urandom(16)
			key = kdf(password,salt)

		encryptor = Cipher(
			algorithm=algorithms.AES(key),
			mode=modes.GCM(iv),
			backend=backends.default_backend(),
			).encryptor()

		cyphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
		cyphertext = cyphertext + iv + encryptor.tag + salt

		return cyphertext
	except:
		return None

def encryptWithHash(plaintext,hash,salt):
	return __encrpt(plaintext,key=hash,salt=salt)
	
def encryptWithPassword(plaintext,password):
	return __encrpt(plaintext,password=password)


def kdf(password,salt=None):
	if salt == None:
		salt = os.urandom(16)
	
	hash = argon2.hash_password_raw(
			time_cost=16,
			memory_cost=2**15,
			parallelism=8,
			hash_len=32,
			password=password.encode(),
			salt=salt
			)
	return hash
