print(''' WELCOME TO THE CALL CENTRE

    PLease choose which sim did you used to call:
    1.NTC
    2.Ncell''')
sim = input('Enter the name of the sim:')
sim2 = input('Enter to which sim did you call:')
duration = int(input('Enter for how long did the call go:'))

if sim == 'NTC' and sim2 == 'NTC':
    if duration <= 10:
        bonus = 2
    elif 10 < duration <= 20:
        bonus = 4
    elif 20 < duration <= 30:
        bonus = 6
    elif 30 < duration <= 40:
        bonus = 8
    elif 40 < duration <= 50:
        bonus = 10
    elif 50 < duration <= 60:
        bonus = 12
    elif 60 < duration <= 70:
        bonus = 14
    elif 70 < duration <= 80:
        bonus = 16
    elif 80 < duration <= 90:
        bonus = 18
    elif 90 < duration == 100:
        bonus = 20
elif sim == 'NTC' and sim2 == 'Ncell':
    if duration <= 10:
        bonus = 5
    elif 10 < duration <= 20:
        bonus = 10
    elif 20 < duration <= 30:
        bonus = 15
    elif 30 < duration <= 40:
        bonus = 20
    elif 40 < duration <= 50:
        bonus = 25
    elif 50 < duration <= 60:
        bonus = 30
    elif 60 < duration <= 70:
        bonus = 35
    elif 70 < duration <= 80:
        bonus = 40
    elif 80 < duration <= 90:
        bonus = 45
    elif 90 < duration == 100:
        bonus = 50
elif sim == 'Ncell' and sim2 == 'Ncell':
    if duration <= 10:
        bonus = 1
    elif 10 < duration <= 20:
        bonus = 2
    elif 20 < duration <= 30:
        bonus = 3
    elif 30 < duration <= 40:
        bonus = 4
    elif 40 < duration <= 50:
        bonus = 5
    elif 50 < duration <= 60:
        bonus = 6
    elif 60 < duration <= 70:
        bonus = 7
    elif 70 < duration <= 80:
        bonus = 8
    elif 80 < duration <= 90:
        bonus = 9
    elif 90 < duration == 100:
        bonus = 10
elif sim == 'Ncell' and sim2 == 'NTC':
    if duration <= 10:
        bonus = 6.5
    elif 10 < duration <= 20:
        bonus = 13
    elif 20 < duration <= 30:
        bonus = 19.5
    elif 30 < duration <= 40:
        bonus = 26
    elif 40 < duration <= 50:
        bonus = 32.5
    elif 50 < duration <= 60:
        bonus = 39
    elif 60 < duration <= 70:
        bonus = 45.5
    elif 70 < duration <= 80:
        bonus = 52
    elif 80 < duration <= 90:
        bonus = 58.5
    elif 90 < duration == 100:
        bonus = 65
else:
    print('Invalid information inputted.')
