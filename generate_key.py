from Crypto.PublicKey import RSA

key = RSA.generate(1024)
f = open('rsakey','w')
f.write(key.exportKey('PEM'))
f.close()
