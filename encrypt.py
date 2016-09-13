import hashlib

m = hashlib.new('DSA')
plaintext = "text".encode('utf-8')

m.update(plaintext)
print(m.hexdigest())
