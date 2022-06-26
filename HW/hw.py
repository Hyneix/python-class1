print("             WELCOME TO COMPUTER BAZAAR")
print("""Choose which laptop you want to buy:
        PRODUCT NAME    COST PRICE
        1.ASUS          Rs 1,00,000
        2.APPLE         Rs 2,00,000
        3.SAMSUNG       Rs 50,000
        4.ACER          Rs 1,00,000""")

product = input("Enter the product name:")

Quantity = int(input('How many do you want:'))

if product == "ASUS" :
    total = 100000*Quantity
elif product == "APPLE":
    total = 200000*Quantity
elif product == "SAMSUNG":
    total = 50000*Quantity
elif product == "ACER":
    total = 100000*Quantity

print('''Delivery option
        1.At House      (Rs 1,000)
        2.Pick up''')
Delivery = input('Enter delivery option :')
if Delivery == "At House":
    charge = 1000
    print('''Chose your location:
            1.Kathmandu         (13% VAT)
            2.Lalitpur
            3.Pokhara''')
    location = input("Enter your location:")
    VAT_amount = (13/100) * total
else:
    charge = 0
    VAT_amount = 0


print("""How do you want to receive your product:
             1.In a Bag         (Rs 1,000)
             2.Plastic Wrap     (Rs 5,000)
             3,Gift Wrap        (Rs 5,000)
             4.None                   """)
Packing = input("chose any one of above option:")
if Packing == "In a Bag":
        Pack = 1000
elif Packing == "Plastic Wrap":
        pack = 5000
elif Packing == "Gift Wrap":
        pack = 5000
else:
        pack = 0

GrandTotal = total + VAT_amount + charge + pack

print(f'''      TOTAL:{total}
          QUANTITY:{Quantity}
          TAX AMOUNT:{VAT_amount}
          GRAND TOTAL = {GrandTotal}''')