class Laptops:
    L_name = 0
    price = 0
    location = 0
    VAT_amount = 0
    Packing = 0
    Delivery = 0
    Total = 0

    def name(self):
        print(''''=====WELCOME TO LAPTOP BAZAAR=====
        CHOSE THE LAPTOP YOU WANT TO BUY:
        Laptop Name             Price
        1.ASUS              Rs 1,00,000
        2.ACER              Rs 90,000
        3.MSI               Rs 1,00,000
        4.DELL              Rs 80,000
        5.APPLE             Rs 2,00,000''')
        self.L_name = input('Enter the laptop name: ')
        if self.L_name == 'ASUS':
            self.price = 100000
        elif self.L_name == 'ACER':
            self.price = 90000
        elif self.L_name == 'MSI':
            self.price = 100000
        elif self.L_name == 'DELL':
            self.price = 80000
        elif self.L_name == 'APPLE':
            self.price = 200000
        else:
            print('Wrong Input')
        return [self.L_name, self.price]

    def Delivery_Package(self):

        print('''Delivery option
                1.At House      (Rs 1,000)
                2.Pick up''')
        self.Delivery = input('Enter delivery option :')
        if self.Delivery == "At House":
            self.price += 1000
            print('''Chose your location:
                    1.Kathmandu         (13% VAT)
                    2.Lalitpur
                    3.Pokhara''')
            self.location = input("Enter your location:")
            self.VAT_amount = (13 / 100) * self.price

        print("""How do you want to receive your product:
                     1.In a Bag         (Rs 1,000)
                     2.Plastic Wrap     (Rs 5,000)
                     3,Gift Wrap        (Rs 5,000)
                     4.None                   """)
        self.Packing = input("chose any one of above option:")
        if self.Packing == "In a Bag":
            self.price += 1000
        elif self.Packing == "Plastic Wrap":
            self.price += 5000
        elif self.Packing == "Gift Wrap":
            self.price += 5000
        else:
            self.pack = 0
        return [self.VAT_amount, self.location, self.price, self.L_name, self.Delivery]

    def Grand_Total(self):
        a = self.Delivery_Package()
        self.Total = a[0] + a[2]
        print(f'''TOTAL:{self.Total}
        TAX AMOUNT:{self.VAT_amount}''')


obj = Laptops()
obj.name()
obj.Grand_Total()
