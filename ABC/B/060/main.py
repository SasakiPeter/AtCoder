a, b, c = map(int, input().split())
#  a*n%b==c これを満たすnがあるかどうか
# nは整数でなければならない
# a*n = b*m+c これを満たすn,mがないと

flag = False
for n in range(101):
    for m in range(101):
        if a*n == b*m+c:
            flag = True
            break
print('YES' if flag else 'NO')

# なにこれすごい
# anyは引数にあるいずれかがTrueならばTrue!!!
# print('YES' if any((a*i) % b == c for i in range(1, b+1)) else 'NO')
