l = []

N = int(input())

# loop to N
for i in range(N):
    command = input().split()

    if command[0] == 'insert':
        l.insert(int(command[1]), int(command[2]))

    elif command[0] == 'print':
        print(l, end='\n')

    elif command[0] == 'remove':
        l.remove(int(command[1]))

    elif command[0] == 'append':
        l.append(int(command[1]))

    elif command[0] == 'sort':
        l.sort()

    elif command[0] == 'pop':
        l.pop()

    elif command[0] == 'reverse':
        l.reverse()
