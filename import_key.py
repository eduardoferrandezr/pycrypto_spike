from Crypto.PublicKey import RSA

# import the private key 
f = open('rsakey','r')
key = RSA.importKey(f.read())
f.close()

# get public key
publickey = key.publickey()

# Encrypt with public key
cyphertext = publickey.encrypt('Hello, Crypto', 0)

# Decrypt with private key
print key.decrypt(cyphertext)

