def simple_intrest():
    global p, r, t
    p = int(input('Enter your Principal:'))
    r = int(input('Enter your rate of interest:'))
    t = int(input('Enter your TIme:'))
    return p, r, t


def simple_interest_1():
    Simple_interest = (p * t * r) / 100
    print(Simple_interest)
    return Simple_interest


simple_intrest()
simple_interest_1()
