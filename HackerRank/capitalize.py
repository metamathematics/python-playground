'''
Ensure that the first and last names of peopl begin with a
capital letter. For example, 'billy butcher  w e' should be capitalized
as 'Billy Butcher  W E'.

Input Format:
A single line of input containing the full name.
'''

s = input()

l = list(s)

nonspace = False
for i in range(len(l)):
    if l[i].isspace():
        nonspace = False
    else:
        if nonspace == False:
            l[i] = l[i].upper()
            nonspace = True

s_upper = ''.join(l)
print(s_upper)
