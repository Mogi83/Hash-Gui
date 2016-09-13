#Created by Scratch45
#Imports
import hashlib

#Creates a new hashlib object using DSA encryption
m = hashlib.new('DSA')

#Asks the user to input the text he or she wants to be encrypted and encodes in utf-8
inputtext = input('Enter text to be encrypted: ')
plaintext = inputtext.encode('utf-8')

#sends the response to m the hashlib object and prints it
m.update(plaintext)
print("Here is your encrypted message: ",m.hexdigest())
