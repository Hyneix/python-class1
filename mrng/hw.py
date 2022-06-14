print("             WELCOME TO COMPUTER BAZAAR")
print("""Which laptop would you like to buy:
        PRODUCT NAME    COST PRICE
        1.ASUS          Rs 1,00,000
        2.APPLE         Rs 2,00,000
        3.SAMSUNG       Rs 50,000
        4.ACER          Rs 1,00,000""")

product = input("Enter the product name:")

if product == "ASUS":
    Quantity = int(input('How many do you want:'))
    total = 100000 * Quantity
elif product == "APPLE":
    Quantity = int(input('How many do you want:'))
    total = 200000 * Quantity
elif product == "SAMSUNG":
    Quantity = int(input('How many do you want:'))
    total = 50000 * Quantity
elif product == "ACER":
    Quantity = int(input('How many do you want:'))
    total = 100000 * Quantity
else:
    print('''Sorry we are out of stock of product you need''')
    exit()

print('''Delivery option
        1.At House      (Rs 1,000)
        2.Pick up       (Free)''')
Delivery = input('Enter how you would like you product to be delivered:')
if Delivery == "At House":
    charge = 1000
    print('''Chose your location:
            1.Kathmandu         (13% VAT)
            2.Lalitpur          (Free)
            3.Pokhara           (Free)
            4.Others''')
    location = input("Enter your location:")
    if location == 'Kathmandu':
        VAT_amount = (13/100) * total
    else:
        VAT_amount = 0
    if location == 'Others':
        location = input("Enter your location:")
else:
    charge = 0
    VAT_amount = 0

print("""How do you want to receive your product:
             1.In a Bag         (Rs 1,000)
             2.Plastic Wrap     (Rs 5,000)
             3.Gift Wrap        (Rs 5,000)
             4.In a Box         (Free)""")
Packing = input("chose any one of above option:")

if Packing == "In a Bag":
    Pack = 1000
elif Packing == "Plastic Wrap":
    pack = 5000
elif Packing == "Gift Wrap":
    pack = 5000
elif Packing == 'In a Box':
    pack = 0

GrandTotal = total + VAT_amount + charge + pack

print(f'''        ====BILL====         
        TOTAL:{total}
        QUANTITY:{Quantity}
        TAX AMOUNT:{VAT_amount}
        GRAND TOTAL = {GrandTotal}''')
