x = float(input('Enter a number:'))
y = float(input('Enter a number:'))
z = float(input('Enter a number:'))

if x > y:
    if x > z:
        print(x, 'is greatest')
    else:
        print(z, 'is greatest')
else:
    if y > z:
        print(y, 'is greatest')
    else:
        print(z, 'is greatest')

Username = input('Enter your username:')
password = input('Enter your password:')

if Username == "admin":
    if password == "admin002":
        print('Welcome')
    else:
        print('Wrong Password')
else:
    print('Wrong username')
