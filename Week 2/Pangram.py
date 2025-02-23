# Write a Python program to check if a passed string is a pangram or not.

import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    s = s.lower()
    s = set(s) 
    return alphabet.issubset(s) 

text = input("Enter a string: ")
if is_pangram(text):
    print("It's a pangram!")
else:
    print("Not a pangram.")
