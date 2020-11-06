'''
Given an integer, n, print the following values for each integer i from 1 to n:
    1. Decimal
    2. Octal
    3. Hex
    4. Binary

The four values must be printed on a single line in the order specified above for each i 
from 1 to n. Each value should be space-padded to match the width of the binary value of n.

Input format
    A single integer denoting n.
'''

n = int(input())

binary = bin(n)[2:]
k = len(binary)

for i in range(1, n + 1):
    print('{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}'.format(i, k))
