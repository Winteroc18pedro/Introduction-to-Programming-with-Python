# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:44:40 2024

@author: pedro
"""
#This programs prompts the user to insert a coin one at a time and each time the user
#inserts a coin, the program informs the user of the amount due.
#The only coins that are accepted are: 5, 10 and 25 cents.

def insert_coin():
    n = 0
    while n < 50:
        amount = int(input("Insert Coin: "))
        if amount not in [5, 10, 25]:
            print("That coin is not allowed!")
        else:
            n = n + amount
            print("Amount Due: ", 50 - n, "cents")
    if 50 - n == 0:
        print("Change owed: 0 cents")
    else:
        print("Change owed: ", abs(50 - n))
        
    
        
    

def main():
    print("Amount due: 50 cents ")
    start = insert_coin()
    print(start)
    

main()

