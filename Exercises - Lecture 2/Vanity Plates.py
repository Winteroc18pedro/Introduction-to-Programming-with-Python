# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:55:51 2024

@author: pedro
"""
###
###In Massachusetts, home to Harvard University, it’s possible to request a vanity license 
#plate for your car, with your choice of letters and numbers instead of random ones. Among 
#the requirements, though, are:

#“All vanity plates must start with at least two letters.”

#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum 
#of 2 characters.”

#“Numbers cannot be used in the middle of a plate; they must come at the end. For example,
#AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 

#The first number used cannot be a ‘0’.”

#“No periods, spaces, or punctuation marks are allowed.”
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    already_number = False
    digits = []
    if s[0].isdigit() or s[1].isdigit():
        return False
    elif not 2 <= len(s) <= 6:
        return False
    for char in s:
        if char in ["_"," ","!","?"]:
            return False
        elif char.isdigit():
            digits.append(char)
            already_number = True
            if int(digits[0]) == 0:
                return False
        elif (not char.isdigit() and already_number):# A number already popped up and so
            return False                           # there mustn't be any letters afterwards
    else:
        return True
        
main()

