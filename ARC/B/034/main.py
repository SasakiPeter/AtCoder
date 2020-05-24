n = int(input())


def f(x):
    res = 0
    for c in str(x):
        res += int(c)
    return res


ans = []
m = max(0, n-9*18)
for i in range(m, n+1):
    if n == i+f(i):
        ans.append(i)
print(len(ans))
for x in ans:
    print(x)
