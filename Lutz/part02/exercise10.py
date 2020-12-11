name = {}
address = {}

name_keys = ['First', 'Middle', 'Last']
address_keys = ['Line 1', 'Line 2', 'City', 'State', 'ZIP']

print('Enter your name.')

for key in name_keys:
    print(key, ': ', end='')
    name[key] = input()


print('\nEnter your age: ', end='')
age = int(input())

print('\nEnter your job title: ', end='')
job = input()


print('\nEnter your address')

for key in address_keys:
    print(key, ': ', end='')
    address[key] = input()


print('\nEnter your email: ', end='')
email = input()

print('\nEnter your phone number: ', end='')
phone = input()


personal_info = [name, age, job, address, email, phone]
print()
for index in range(len(personal_info)):
    if index == 0 or index == 3:
        if index == 0:
            for key in name_keys:
                print(personal_info[index][key], end=' ')

        else:
            for key in address_keys:
                print(personal_info[index][key], end=' ')

    else:
        print()
        print(personal_info[index], end=' ')

print()
