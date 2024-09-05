import random
import string

def generatePassword(length ,num = True ,speChar = True):
    letter = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letter
    if num:
        characters += digits
    if speChar:
        characters += special
        
    pwd = ""
    criteria = False
    has_num = False
    has_special = False
    while (not criteria or len(pwd) < length):
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_num = True
        elif new_char in special:
            has_specials = True
        
        criteria = True
        if num:
            criteria = has_num
        elif speChar:
            criteria = criteria and has_special
        
    return pwd

length = int(input("enter the size of password you want..."))
num = input("do you want to have numbers in it (y/n)?").lower() == "y"
speChar = input("do you want to have special characters in it (y/n)?").lower() == "y"

print("the generated password is : ",generatePassword(length , num , speChar))