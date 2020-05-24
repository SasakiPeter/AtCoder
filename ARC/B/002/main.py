# もっと簡単に解ける
import datetime
fmt = '%Y/%m/%d'
start = datetime.datetime.strptime(input(), fmt)

for i in range(366):
    delta = datetime.timedelta(days=i)
    cur = start+delta
    # y, m, d = map(int, cur.strftime(fmt).split('/'))
    y, m, d = cur.year, cur.month, cur.day
    if y % (m*d) != 0:
        continue
    print(cur.strftime(fmt))
    break

# y, m, d = map(int, input().split('/'))


# divisors = set()
# for i in range(1, int(y**.5)+1):
#     if y % i == 0:
#         divisors |= {i, y//i}

# e30 = (4, 6, 9, 11)


# def is_uruu(y):
#     if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
#         return 29
#     else:
#         return 28


# for month in range(m, 13):
#     if month not in divisors:
#         continue
#     if month == 2:
#         end = is_uruu(y)
#     elif month in e30:
#         end = 30
#     else:
#         end = 31
#     start = d if m == month else 1
#     for day in range(start, end+1):
#         # 2000で4/4とか考えられる
#         # if month == day:
#         #     continue
#         if day not in divisors:
#             continue
#         if y % (month*day) != 0:
#             continue
#         print("/".join(map(lambda x: "{:02}".format(x), (y, month, day))))
#         exit()
# else:
#     print('{}/01/01'.format(y+1))
