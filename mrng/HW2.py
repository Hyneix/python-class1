print('''       WELCOME TO BOOK STORE NEPAL
        PLEASE CHOOSE THE BOOK YOU WANT 
        
        BOOK NAME           AUTHOR's NAME           PRICE
        1.Urgenko Ghoda     Yug Pathak              Rs 650
        2.Pagal premee      Jitendra Sahayogee      Rs 550
        3.Junkiri	        Siddhicharan            Rs 600''')

book_name = input('Enter the name of the book you want to buy:')

if book_name == 'Urgenko Ghoda':
    Quantity = int(input('How many do you want:'))
    book_Price = 650 * Quantity
    Author = 'Yug Pathak'
elif book_name == "Pagal premee":
    Quantity = int(input('How many do you want:'))
    book_Price = 550 * Quantity
    Author = 'Jitendra Sahayogee'
elif book_name == "Junkiri":
    Quantity = int(input('How many do you want:'))
    book_Price = 600 * Quantity
    Author = 'Siddhicharan'
else:
    print("Sorry the book you are looking for is unavailable right now")
    exit()

print('''Delivery option
        1.At House      (Rs 500)
        2.Pick up''')
Delivery = input('Enter delivery option :')
if Delivery == "At House":
    charge = 500
    print('''Chose your location:
            1.Kathmandu         
            2.Lalitpur
            3.Pokhara''')
    location = input("Enter your location:")
else:
    charge = 0

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
elif Packing == 'None':
    pack = 0

total = book_Price + charge + pack
print(f'''       ======BILL======
        Book name = {book_name}
        Author    = {Author}
        Quantity  = {Quantity}
        Total     = {total}''')
