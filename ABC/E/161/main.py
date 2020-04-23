n, k, c = map(int, input().split())
s = input()

# 働かない可能性があるのを記録する
work = [1]*n

rest = 0
for i in range(n):
    if rest:
        rest -= 1
        work[i] = 0
        continue

    if s[i] == 'x':
        work[i] = 0
    elif s[i] == 'o':
        rest = c


rest = 0
for i in reversed(range(n)):
    if rest:
        rest -= 1
        work[i] = 0
        continue
    if s[i] == 'o':
        rest = c

# print(work)

if k < sum(work):
    print()
else:
    for idx, bl in enumerate(work):
        if bl:
            print(idx+1)
