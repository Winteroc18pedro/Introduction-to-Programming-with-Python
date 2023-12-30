# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 18:30:53 2023

@author: pedro
"""

def playback():
    say = input("Tell me something: ").split()
    for word in say:
        print(word,"... ", end="")

playback()

