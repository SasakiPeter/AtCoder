# day = input()
# weekday = ['Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
# print(weekday.index(day)+1 if day in weekday else 0)

# indexはO(n)かかるのでダサい
# こういう時はdictを使って速度O(1)にしよう！
d = {'Mo': 5, 'Tu': 4, 'We': 3, 'Th': 2, 'Fr': 1, 'Sa': 0, 'Su': 0}
print(d[input()[:2]])
