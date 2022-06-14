# # defining a decorator
# def hello_decorator(func):
#     # inner1 is a Wrapper function in
#     # which the argument is called
#
#     # inner function can access the outer local
#     # functions like in this case "func"
#     def inner1():
#         print("Hello, this is before function execution")
#
#         # calling the actual function now
#         # inside the wrapper function.
#         func()
#
#         print("This is after function execution")
#
#     return inner1
#
#
# # defining a function, to be called inside wrapper
# def function_to_be_used():
#     print("This is inside the function !!")
#
#
# # passing 'function_to_be_used' inside the
# # decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)
#
# # calling the function
# function_to_be_used()
x = float(input('Enter any number:'))
y = float(input("Enter any number:"))


def outer(func):
    def inner(x, y):
        if y == 0:
            print("Y is Zero")
        elif x == 0:
            print("X is zero")
            return
        return func(x, y)
    return inner


def check(funcx):
    def great(x, y):
        if x > 100:
            print("X must be less than 100")
            exit()
        elif y > 100:
            print("Y must be less than 100")
            exit()
            return
        return funcx(x, y)
    return great


@outer
@check
def display(x, y):
    print('The output is', x*y)


display(x,y)
