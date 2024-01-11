# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:14:59 2024

@author: pedro
"""

def cost_of_the_meal():
    cost = float(input("How much did the meal cost? "))
    return cost

def percentage():
    percent = int(input("How much would you like to tip in percentage? "))
    return percent/100 #Decimal representation of percentage

def main():
    price = cost_of_the_meal()
    tip_percentage = percentage()
    total_tip = price * tip_percentage
    print("The tip amount is ", end='')
    print(round(total_tip, 1), "euros")
    
main()
        



