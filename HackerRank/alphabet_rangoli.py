'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
The center of the rangoli has the first alphabet letter a, and the boundary has
the Nth alphabet letter (in order).

Input Format
    Only one line of input containing N the size of the rangoli.

Constraints
    0 < N < 27
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
subset = alphabet[:n]

m = 2 * (n - 1)

print('\n')

# Top half
for i in range(0, m + 1, 2):
    print(('-' * (m - i)), end='')

    k = 1
    for j in range(i + 1):
        print(subset[n - k], end='')

        if j < i:
            print('-', end='')
        
        if j < (i / 2):
            k = k + 1
        else:
            k = k - 1

    print(('-' * (m - i)))

# Bottom half
for i in range(m - 2, -2, -2):
    print(('-' * (m - i)), end='')
    
    k = 1
    for j in range(i + 1):
        print(subset[n - k], end='')

        if j < i:
            print('-', end='')
        
        if j < (i / 2):
            k = k + 1
        else:
            k = k - 1

    print(('-' * (m - i)))
