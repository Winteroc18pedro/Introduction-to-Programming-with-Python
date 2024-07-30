# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:08:47 2024

@author: NB30006
"""

#Write a program that shows the nutrition facts for the 19 most popular 
#fruits. It prompts the user to input a fruit and outputs the number of calories
#in that fruit


fruits = {"Apple":130,"Avocado":50,"Banana":110,"Cantaloupe":50,"Grapefruit":60,
          "Grapes":90,"Kiwi":90, "Lemon":15,"Lime":20,"Nectarine":60,"Orange":80,
          "Peach":60,"Pear":100,"Pineapple":50,"Plum":70,"Strawberry":50,
          "Cherries":100,"Tangerine":50,"Watermelon":80}

def get_calories(fruit):
    if fruit.capitalize() in fruits:
        print("Calories: ", fruits[fruit.capitalize()])
    else:
        print("That is not a fruit or it is misspelled")

def main():
    item = input("Type here the name of the fruit: ")
    get_calories(item)
    

main()
