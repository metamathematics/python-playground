'''
Make a door mat with the following specifications:
    - Mat size is NxM (where N is an odd natural number, and M is 3 times N)
    - The design should have 'WELCOME' written in the center
    - The design patter should only use |, ., and - characters

Input Format
    - A single line containg the space separated values of N and M
'''

inputs = input()

N, M = inputs.split()
N = int(N)
M = int(M)

cross = 1
dash = int((M - (cross * 3)) / 2)

print()

while dash >= 3:
    print(('-' * dash) + ('.|.' * cross) + ('-' * dash))
    cross = cross + 2
    dash = dash - 3

k = int((M - 7) / 2)
print(('-' * k) + 'WELCOME' + ('-' * k))

cross = cross - 2
dash = dash + 3
while cross >= 1:
    print(('-' * dash) + ('.|.' * cross) + ('-' * dash))
    cross = cross - 2
    dash = dash + 3
