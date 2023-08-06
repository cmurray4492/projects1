"""Regex 1 File"""
import re

pattern = re.compile(r"")
my_string = input('Enter a string, with digits: ')
# with the + all consective digits are repalced with one character
pattern = re.compile(r"[0-9]+")
# if no + all digits are repalced with a character
# pattern = re.compile(r"[0-9]")
result = pattern.sub("_", my_string)
print(result)
