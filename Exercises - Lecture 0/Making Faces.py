# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:47:04 2024

@author: pedro
"""
#I am going to create a program that converts ":)" and ":(" into their respective emojis.

# I installed the emoji module using "pip install emoji"

import emoji

#https://www.geeksforgeeks.org/python-program-to-print-emojis/
#The website above as the code for the most common emojis.

#What is String replace() Method?
#String replace() is a built-in function in Python and it is used to replace 
#a substring with another string. It will replace every occurrence of that
#substring, so it should be used with caution.

#string.replace(old, new, count)

#Parameters: 
#old – old substring you want to replace.
#new – new substring which would replace the old substring.
#count – (Optional ) the number of times you want to replace the old substring with the new substring. 


def convert(text):
    if ":)" in text:
        new = text.replace(":)",emoji.emojize(":slightly_smiling_face:"))
        print(new)
    elif ":(" in text:
        new = text.replace(":(",emoji.emojize(":slightly_frowning_face:"))
        print(new)
    else:
        print(text)
        

def main():
    text = input("Say something with an emoji: ")
    convert(text)
    
main()



