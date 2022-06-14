# Wap to know the greatest among 2 number:
# x = float(input("Enter a number:"))
# y = float(input("Enter another number:"))
# if x > y:
#     print(x, "is greater than", y)
# else:
#     print(y, "is greater than", x)

#  wap to enter the age and welcome the people of age 18-40 in the party:
# a = int(input("Enter Your age"))
# if 18 <= a <= 40:
#     print("Welcome to the party")
# else:
#     print("You cannot enter the party ")

# wap to find out if the number is od or even:
# b = int(input("Enter a number:"))
# if b % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# Wap to enter username and password:
# username = input("Enter your username:")
# password = input("Enter your password:")
#
# if (username == "admin") and (password == "admin002"):
#     print(f"Welcome {username}")
# else:
#     print("Incorrect username or password")

# WAP to input Marks and give their grades:
nep = float(input('Enter your marks in nepali:'))
if nep > 100:
    print("Invalid Marks")
    exit()

eng = float(input("Enter your marks in english:"))
if eng > 100:
    print("Invalid Marks")
    exit()
comp = float(input('Enter your marks in Computer:'))
if comp > 100:
    print("Invalid Marks")
    exit()
math = float(input('Enter your marks in maths:'))
if math > 100:
    print("Invalid Marks")
    exit()
sci = float(input('Enter your marks in science:'))
if sci > 100:
    print('Invalid Marks')
    exit()
total = nep + eng + comp + math + sci
percentage = total / 5
print(f"total:{total} Percentage:{percentage}")
if 35 <= percentage <= 45:
    print("C")
elif 45 < percentage <= 60:
    print("B")
elif 60 < percentage <= 80:
    print("A")
elif 80 < percentage <= 100:
    print("A+")
else:
    print("D")

# WAP to know if the number is divisible by 3 or 5 or with both of them or not divisible by both :
a = int(input('Enter a number'))
if a % 3 == 0 and a % 5 == 0:
    print(f"{a} is divisible by both 3 and 5")
elif a % 3 == 0 and a % 5 != 0:
    print(f"{a} is divisible by only 3")
elif a % 3 != 0 and a % 5 == 0:
    print(f"{a} is divisible by only 5")
else:
    print('The number is not divisible by both 3 and 5')

#
