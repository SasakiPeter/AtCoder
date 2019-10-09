n,  k = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10**9+7

# 内部の転倒数
ls = a[:]
inner = 0
while ls:
    x = ls.pop(0)
    inner += sum(1 if x > y else 0 for y in ls)

# 外部の転倒数
outer = 0
for x in a:
    for y in a:
        if x > y:
            outer += 1


print((inner*k + outer*(k-1)*k//2) % MOD)
