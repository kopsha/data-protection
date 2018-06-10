from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64decode, b64encode

KEYSIZE = 1024

def decrypt(private_key, message):
	key = RSA.importKey(private_key)
	cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
	return cipher.decrypt(b64decode(message))

def encrypt(public_key, message):
	key = RSA.importKey(public_key)
	cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
	return b64encode(cipher.encrypt(message))

def generate_keys():
	key_pair = RSA.generate(KEYSIZE)
	return key_pair.exportKey() , key_pair.publickey().exportKey()

def get_public_key_backend():
	f = open('public_key_backend.pem','r')
	key = f.read()
	f.close()
	return key

def get_private_key_backend():
	f = open('private_key_backend.pem','r')
	key = f.read().replace('\n', '')
	f.close()
	return key

def get_public_key_client():
	f = open('public_key_client.pem','r')
	key = f.read().replace('\n', '')
	f.close()
	return key

def get_private_key_client():
	f = open('private_key_client.pem','r')
	key = f.read()
	f.close()
	return key
