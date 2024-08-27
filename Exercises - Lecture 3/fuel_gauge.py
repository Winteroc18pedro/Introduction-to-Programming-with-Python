# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:47:06 2024

@author: NB30006
"""

#Write a program that prompts the user for a fraction formatted as X/Y wherein
#each of the X and Y are integers and then outputs as a percentage rounded to
#the nearest integer, how much fuel is in the tank. If 1% or less remains
#the output is "E" to indicate that the tank is essentially empty, if 99% or more
#remains the output is "F" to indicate that the tank is essentially full.
#If X and Y are not integers,X is greater than Y or Y is 0, prompt the user
#again

def fraction(x, y):
    return (x/y) * 100

def fraction(x, y):
    return (x/y) * 100

def main():
    while True:
        try:
           x = int(input("What's the value of x?"))
           y = int(input("What's the value of y?"))
           if y == 0:
               print("y cannot be zero")
           elif x > y:
               print("x cannot be greater than y")
               continue
           percentage = round(fraction(x,y))
           if percentage < 1:
               print("E")
           elif percentage > 99:
               print("F")
           else:
               break
        except ValueError:
            print("That's not an integer. Try again")
    print(f"{percentage}%")

main()


