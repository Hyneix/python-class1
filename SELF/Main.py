# def Main(*args):
#     print(args)
# # args will be a tuple containing all values that are passed in
#
#
# Main(1,2,3,4,5)

# def Mains(**kwargs):
#     print(kwargs)
# # kwargs will be a dictionary containing the names as keys and the values as values
#
#
# Mains(value1=1, value2=2)

# def fnu(**kwargs):
#     print(len(kwargs))
#
# fnu(a=1,b=2)

# def greeting():
#     print("Hello")
#
#
# greeting()

# greet = lambda : 'Hello'   # One line function.
# print(greet())

# def fun(name):
#     print(name)
#
#
# fun('ram')


#               Mistake
# x = int(input('Enter a number:'))
# y = int(input('Enter another number:'))
#
#
# def Check(funx):
#
#     def checking(x,y):
#         if x % 2 == 0 :
#             print(x, 'is even number.')
#         else:
#             print(x, 'is odd number.')
#
#         if y % 2 == 0:
#             print(y, 'is even number.')
#         else:
#             print(y, 'is odd number.')
#          return funx(x, y)
#     return checking
#
# @Check
# def display(x,y):
#     print(f'The addition if {x} and {y} is', x*y)
