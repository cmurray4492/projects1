"""Regex 2 Findall"""
import re

my_string = input('Enter a string, with digits: ')
# result = re.findall(r"\d", my_string)
result = re.findall(r"\d+", my_string)
print(result)
