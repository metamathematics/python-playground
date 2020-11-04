'''
You are given a string and a width w.
Your task is to wrap the string into a paragraph of width w.
'''
import textwrap

string = input()
width = int(input())

result = textwrap.fill(string, width)
print(result)
