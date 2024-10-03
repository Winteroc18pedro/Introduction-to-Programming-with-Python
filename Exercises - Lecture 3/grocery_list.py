# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Write a program that prompts the user for items at a grocery shop, one per
#line, until the user inputs control + d (which is a common way of ending
#one's input to a program). Then output the user's list all in uppercase
#sorted alphabetically by item, prefixing each line with the number of times
#the user inputted that item

def items():
    item_dict = {}
    try:
        while True:
            item = input("What do you want to buy? ")
            if item not in item_dict:
                item_dict[item] = 1
            elif item in item_dict:
                item_dict[item] += 1
    except EOFError:
        print("\nEnd of input detected. Exiting program")
    print(item_dict)
    return item_dict

def sort_and_organize(dictionary):
    print(sorted(dictionary.items()))
    return sorted(dictionary.items())
        

if __name__ == "__main__":
    a = items()
    b = sort_and_organize(a)
    for key, value in b:
       print(value, key.upper())

