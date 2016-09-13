#Created by Scratch45
#Imports
import hashlib
inputText = " "
plainText = " "

#Main class, hashs text that is inputed
def main():
    
    hashType = input("Please enter a encryption type: ")
    haType = hashType.encode("utf-8")
    m = hashlib.new(encryptType)
    

#Asks the user to input the text he or she wants to be hashed and encodes in utf-8
    inputText = input('Enter text to be encrypted: ')
    plaintext = inputText.encode('utf-8')

#sends the response to m the hashlib object and prints it
    m.update(plaintext)
    print("Here is your encrypted message: ",m.hexdigest())
#Lists accepted Encrytpion types
def hashTypes():
    print ("Accepted hash types are sha(1,224,256,384,512) md4, md5, whirlpool,DSA, and ripemd160")
#Gives users methods they can call
def help():
    print ("Methods in encrypt.py, main(), hashTypes()")



