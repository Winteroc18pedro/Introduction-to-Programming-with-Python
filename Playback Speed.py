# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 18:30:53 2023

@author: pedro
"""
#This program prompts the user for input and then outputs that same input,
#replacing each space with ...

def playback():
    say = input("Tell me something: ").split()
    for word in say:
        print(word,"... ", end="")

playback()

#split() : This is the most common method for splitting a text into a list. 

