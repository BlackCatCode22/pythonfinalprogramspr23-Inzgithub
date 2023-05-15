
# import libraries as needed

import random
# https://www.w3schools.com/python/module_random.asp

print('Password Generator Program')

#creating a string variable that will contain all the characters used to generate a password. 
validCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*&-_+=?'

passwordsGenerated = input('Please state how many passwords you need: ')
passwordsGenerated = int(passwordsGenerated)

passwordLength = input("Please state the length of your password: ")
passwordLength = int(passwordLength)

print('\nPasswords Generated.....')

for passwords in range(passwordsGenerated):
    passwords = " "
    for c in range(passwordLength):
        #random.choice is using the RANDOM library to select a random set of letters from the validCharacters variable
        passwords += random.choice(validCharacters)
    print(passwords)

print('\n1Thank you for using Password Generator Program')