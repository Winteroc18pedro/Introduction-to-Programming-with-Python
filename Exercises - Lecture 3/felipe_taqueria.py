# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:43:21 2024

@author: NB30006
"""

#Felipe's taqueria offers a menu of entrees as follows:
    
items = {"Baja Taco": 4.25,
 "Burrito": 7.50,
 "Bowl": 8.50,
 "Nachos": 11.00,
 "Quesadilla": 8.50,
 "Super Burrito": 8.50,
 "Super Quesadilla": 9.50,
 "Taco": 3.00,
 "Tortilla Salad": 8.0}

#Implement a program that enables the user to place an order, prompting them for items
#one per line, until the user inputs control d (It is a common way of ending one's input
#to a program). After each inputted item,  display the total cost of all the items
#inputted thus far followed by a dollar sign and rounded to two decimal places.
#Treat the input case insensitively and ignore an input that is not an item on the list
#Assume that every item in the list will be titlecased.

def place():
    order = []  #This list has to be initialized outside of the loop
    while True: #otherwise if it is inside, it will be re-initialized as an empty list
        try:    #at the beginning of each iteration
            x = input("Look at the menu and tell me which item(s) do you want? ").title()
            if x not in items:
                print("That is not in the menu")
                continue
            elif x in items:
                print(f"{x} costs {items[x]}")
                order.append(x)
        except EOFError: #After pressing control + d, it will exit the program
            print("\nEOF detected. Exiting the program.")
            break
    return order
        
def price(your_order):
    total = 0
    for i in your_order:
        total += items[i] 
    return total
    
    
    
def main():
    my_order = place()
    total_price = price(my_order)
    print("The total will be", total_price, "dollars")
    
    
    
main()
        
    
