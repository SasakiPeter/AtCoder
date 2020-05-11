# 1年366日ある
from itertools import accumulate
days = [0]*366
for i in range(366):
    if i % 7 == 0 or i % 7 == 6:
        days[i] = 1

months = [0]+list(accumulate([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
# print(months)

n = int(input())
for _ in range(n):
    month, day = map(lambda x: int(x)-1, input().split('/'))
    idx = months[month]+day
    while True:
        if not days[idx]:
            days[idx] = 1
            break
        idx += 1
        if 365 < idx:
            break

print(max(map(len, "".join(map(str, days)).replace('0', ' ').split())))
