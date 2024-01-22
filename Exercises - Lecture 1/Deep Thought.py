# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:09:08 2024

@author: pedro
"""
#This program asks a very famous question and the answer is only one: 42.

def question():
    n = input("What's the answer to the great question of life, the universe and everything? ")
    return n

def main():
    answer = question()
    if int(answer) == 42 or answer == "forty two":
        print("Yes")
    else:
        print("No")
        
        
main()
  