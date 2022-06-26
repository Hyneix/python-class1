times = int(input('Enter how many times do you want to type:'))

for i in range(times):
    nep = float(input('Enter your marks in Nepali:'))
    eng = float(input('Enter your marks in English:'))
    math = float(input('Enter your marks in Maths:'))
    sci = float(input('Enter your marks in Science:'))
    soc = float(input('Enter your marks in Social:'))

    total = nep + eng + math + sci + soc
    print('The total marks obtained out of 500 is ', total)

    percent = (total / 500) * 100
    print("Marks obtained in percentage is =", percent, '%')

    if 97 <= percent == 100:
        print('You have secured A+')
    elif 93 <= percent >= 96:
        print("You secured A")
    elif 90 <= percent >= 92:
        print('You have secured A-')
    elif 87 <= percent >= 89:
        print('You have secured B+')
    elif 83 <= percent >= 86:
        print('You have secured B')
    elif 80 <= percent >= 82:
        print('You have secured B-')
    elif 77 <= percent >= 79:
        print('You have secured C+')
    elif 73 <= percent >= 76:
        print('You have secured C')
    elif 70 <= percent >= 72:
        print('You have secured C-')
    elif percent <= 71:
        print('You secured D')