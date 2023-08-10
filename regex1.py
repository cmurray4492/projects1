"""Regex 1 File"""
import re

pattern = re.compile(r"")
my_string = input('Enter a string, with digits: ')
# with the + all consective digits are repalced with one character
# pattern = re.compile(r"[0-9]+")
pattern = re.compile(r"\D+")  # or \d for digits \D for letters
# if no + all digits are repalced with a character
# pattern = re.compile(r"[0-9]")
# result = pattern.sub("_", my_string)
result = pattern.sub("$", my_string)
print(result)
