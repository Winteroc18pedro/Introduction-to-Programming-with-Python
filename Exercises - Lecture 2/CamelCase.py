# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:16:13 2024

@author: pedro
"""

#This program prompts the user for input in camel case and outputs the corresponding name
#in snake case

#   preferredFirstName    --->   preferred_first_name


def camel_to_snake(word):
    new_word = ""
    for i in word:
        if i.islower():
            new_word = new_word + i
        if i.isupper():
            new_word = new_word + "_" + i.lower()
    return new_word

    
    
def main():
    x = input("What's the variable name in Camel Case ? ")
    variable = camel_to_snake(x)
    print("Snake Case: ", variable)
    
    
main()