#! python3
# StrongPasswordDetection - make sure the password string is strong

import re

print("Please enter a password to check the strength:")
password = input()

#TODO: function to check password strength
def passwordStrength(password):
    if lengthEight.search(password) == None:
        print("String character is less than 8. Not strong.")
    elif stringUpper.search(password) == None:
        print("String character doesn't contain Upper Case. Not strong.")
    elif stringLower.search(password) == None:
        print("String character doesn't contain Lower Case. Not Strong.")
    elif stringDigit.search(password) == None:
        print("String character doesn't contain digit. Not strong.")
    else:
        print("Password is strong.")
        
#TODO: regex to check length of the string is 8 or more
lengthEight = re.compile(r'^[a-zA-Z0-9]{8,}$')

#TODO: regex to check string contain upper case
stringUpper = re.compile(r'[A-Z]')

#TODO: regex to check if string contains lower case
stringLower = re.compile(r'[a-z]')

#TODO: regex to check if string has atleast one digit.
stringDigit = re.compile(r'\d')


passwordStrength(password)
