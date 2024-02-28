# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:20:13 2023

@author: pedro
"""
#This program prompts the user to say something and it outputs the same message without the
#vowels

def take_out_vowels(word):
    vowel = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    new_word = ""
    for v in word:
        if v in vowel:
            continue
        elif v not in vowel:
            new_word = new_word + v
    return new_word

def main():
    n = input("Tell me something  and I'll do a magic trick: ")
    without_vowels = take_out_vowels(n)
    print(without_vowels)

main()

    