#!/usr/bin/python3
"""Yogesh Mhatre
   Custom Lab 01 Solution"""

import zipfile

def main():
    """runtime code"""

    iszip = input("What is the file you would like to examine (full or relative path)? ")

    if zipfile.is_zipfile(iszip): #returns true if the file is zip file
        print("Yep! That is a 'zip' file.")
    else:
        print("No. That is not a 'zip' file.")

if __name__ == "__main__":
    main()
