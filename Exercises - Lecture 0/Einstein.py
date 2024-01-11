# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 20:21:07 2024

@author: pedro
"""
#Einstein's special theory of relativity
#Einstein proved that energy equals mass times the speed of light

def einstein(m):
    c = 300000000 #m/s   where c is the speed of light
    E = m * (c**2)  #E stands for (Energy) and m stands for mass (in Kilograms)
    return E

def main():
    mass = float(input("What's the mass? "))  
    Energy = einstein(mass)
    print(Energy)

main()



