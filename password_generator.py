import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c_letters = list(letters.upper())
s_letters = list(letters.lower())
symbels = ['(',')','-','_','~','!','@','<','>','?',';','\'','\"',':','/','|','#','$','%','&','*','+','`','=','^']
numbers = list('0123456789')

password_characters = c_letters.copy()
password_characters.extend(s_letters)
password_characters.extend(symbels)
password_characters.extend(numbers)


len_pwd = 0
while True:
    try:
        len_pwd = int(input('Please enter password length (don\'t over 1024 characters):  '))
        if len_pwd > 1024:
            print('Exceed password limit, PLEASE TRY AGAIN')
            continue
        break

    except ValueError:
        print('Please enter Number')

password = ''
for x in range(len_pwd):
    password += password_characters[random.randint(0,len(password_characters)-1)]

print(password)
    