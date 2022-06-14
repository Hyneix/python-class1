# To arrange elements use sort (sorting  for string and integer must be done separately but code is same for both)
data = ["zebra", 'ram', 'shyam']
print(type(data))
data.sort(reverse=False)
print("The data is in ascending order=", data)
data.sort(reverse=True)
print("The data is in descending order", data)

# To add data at last use append
users = ["ram", "shyam", "hari"]
print(users)
users.append('lela')
print(users)

# To any data from the list (use index number,in list index starts from 0 )
ur = ['shyam', 'ram', 'sita']
# print(ur[index number])
print(ur[0])
hello = [
    ['ram', 'shyam'],  # 0- index (again-->ram=0,shyam=1)
    ['hari', 'lal'],  # 1- index (again-->hari=0,lal=1)
    ['lela', 'ramu']  # 2- index (again-->lela=0,ramu=1)
]
# print(hello[index][2nd index])
print(hello[0][0])

# To clear all the data of the list use clear option
we = ['ram', 'shyam']
print(we)
print(we.clear())

# To count occurrence of same name or number use count
co = ['ram', 123, 'hari', 123, 'shyam', 'hari']
print("The count of occurrence of same word in list =", co.count('hari'))

# To count the length of the  list use len()
co = ['ram', 123, 'hari', 123, 'shyam', 'hari']
print('The total number of elements in a list =', len(co))

# To know the id of the elements use id
a = 123
print("The unique if of variable a is ", id(a))

# To find the index number of the elements use index()
rs = ['ram', 'shyam', 'ramu', 123]
print("The index number is =", rs.index('ramu'))

# To remove specific data from table use remove
df= ['ram', 'shyam', 123]
print('The data after removing something =', df)
df.remove(123)
print('After removing a data = ', df)

# To insert data in the list use insert()
re = ['ram', 'shyam', 123]
# re.insert(index number, data to insert)
print('The data before inserting =', re)
re.insert(1, 'hari')
print("After inserting a data =", re)

# To Extend the elements in list use extend()
qu = ['ram','shyam',123]
print('The data before extending it =', qu)
# qu.extend(data to insert, data to insert)
qu.extend(['hi', 'hello'])
print('The data after inserting =', qu)
