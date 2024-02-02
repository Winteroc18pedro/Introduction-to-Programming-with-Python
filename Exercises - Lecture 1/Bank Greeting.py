# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:32:47 2024

@author: pedro
"""
#This program prompts the banker for a greeting and then depending on the output of the banker
#the client will get a certain amount of money ( or none at all ).

def bank_greeting():
    return input("Greeting: ")
    

def main():
    greeting = bank_greeting().capitalize()
    split_greeting = greeting.split()
    if split_greeting[0] == "Hello":
        print("You get 0 dollars")
    elif greeting[0] == "H":
        print("You get 20 dollars")
    else:
        print("You get 100 dollars")

main()




    


