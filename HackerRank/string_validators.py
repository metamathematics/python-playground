'''
You are given a string s.
Your task is to find out if the string s contains:
    alphanumeric characters, alphabetical characters,
    digits, lowercase and uppercase characters.
'''

alnu = False
alpha = False
digit = False
lower = False
upper = False
string = input()

for s in string:
    if s.isalnum():
        alnu = True
    if s.isalpha():
        alpha = True
    if s.isdigit():
        digit = True
    if s.islower():
        lower = True
    if s.isupper():
        upper = True

print(alnu)
print(alpha)
print(digit)
print(lower)
print(upper)
