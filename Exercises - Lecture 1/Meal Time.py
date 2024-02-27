# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:02:11 2024

@author: pedro
"""
#It is a function that prompts the user for the current time and outputs a message depending
#on what time it is.
def convert(n):
    return n.replace(":",".")

def main():
    time = input("What time is it? ")
    t = float(convert(time))
    if 7.0 <= t <= 8.0:
        print("it's breakfast time!")
    elif 12.0 <= t <= 13.0:
        print("it's lunch time!")
    elif 18.0 <= t <= 19.0:
        print("it's dinner time!")
    else:
        print("it's not time to eat!")

main()