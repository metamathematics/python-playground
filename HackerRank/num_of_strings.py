# Find the number of times that the substring occurs ina given string

def find_all(string, substring):
    count = 0
    
    index = string.find(substring)
    while index != -1:
        count = count + 1

        if index + 1 < len(string):
            string = string[index+1:]
            index = string.find(substring)
        else:
            index = -1
    
    return count

x = input()
y = input()

print(find_all(x, y))
