# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:08:16 2024

@author: pedro
"""
#This program prompts the user for the name of the file and outputs the file's media type.


def file_extension(name):
    if ".gif" in name:
        return "image/gif"
    elif ".jpg" in name or ".jpeg" in name:
        return "image/jpg"
    elif ".png" in name:
        return "image/png"
    elif ".pdf" in name:
        return "application/pdf"
    elif ".txt" in name:
        return "text/plain"
    elif ".zip" in name:
        return "application/zip"
    else:
        return "application/octet-stream"
        
def main():
    Name_Of_The_File = input("What's the name of the file including the file extension? ")
    print("File Extension: ", file_extension(Name_Of_The_File))
    
                             


main()