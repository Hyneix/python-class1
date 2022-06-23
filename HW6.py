import datetime

year = int(input('When is your birthday? [YY] '))
month = int(input('When is your birthday? [MM] '))
day = int(input('When is your birthday? [DD] '))
gog = datetime.datetime.now().date()
obj = datetime.date(year, month, day)
lo = obj - gog
goal = lo
print(goal)
print(gog)
print(obj)


# jobs = [
#     {'id': 1, 'title': 'python developer', 'created_at': '2022-06-10', 'expire': '2022-06-25'},
#     {'id': 1, 'title': 'php developer', 'created_at': '2022-05-10', 'expire': '2022-07-25'},
#     {'id': 1, 'title': 'django developer', 'created_at': '2022-04-10', 'expire': '2022-05-25'},
# ]
# for i in range(3):
#     g = jobs[i]['created_at']
#     b = jobs[i]['expire']
#     print(g)
#     print(b)
#     nie = int(b[6]) - int(g[6])
#     k = (int(b[8]) * 10 + int(b[9])) - (int(g[8]) * 10 + int(g[9]))
#     print(f'''The time left for your job to expire is {nie} months and {k} days.''')
