# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:43:37 2024

@author: pedro
"""
# This program is a simple calculator

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def main():
    x = float(input("What's x? "))
    y = float(input("What's y? "))
    choice = input("Choose one of the following: \nA - Addition \nS - Subtraction \nM - Multiplication \nD - Division\n")
    if choice == "A":
        print(x, "+", y, "=", addition(x, y))
    elif choice ==  "S":
        print(x, "-", y, "=", subtraction(x, y))
    elif choice == "M":
        print(x, "*", y, "=", multiplication(x, y))
    elif choice == "D":
        print(x, "/", y, "=", division(x, y))
    
main() 