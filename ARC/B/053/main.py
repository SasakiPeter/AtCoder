from collections import Counter
s = input()
c = Counter(s)
# print(c)
cnt = 0
for k, v in c.items():
    if v & 1:
        cnt += 1
        c[k] -= 1

SUM = sum(v for v in c.values())
# print(1+SUM//cnt)
# print(c)
# print(SUM, cnt)

if cnt == 0:
    print(SUM)
else:
    print(SUM//2//cnt*2+1)
