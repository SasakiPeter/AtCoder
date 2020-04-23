n, h = map(int, input().split())
# a = [0]*n
# b = [0]*n
# for i in range(n):
#     a[i], b[i] = map(int, input().split())

# これカッチョいい
ab = [list(map(int, input().split())) for _ in range(n)]
a, b = zip(*ab)

A = max(a)
B = sorted([x for x in b if x > A], reverse=True)


cnt = 0
damage = 0
for b in B:
    cnt += 1
    damage += b
    if damage >= h:
        break
else:
    cnt += -(-(h-damage)//A)
print(cnt)
