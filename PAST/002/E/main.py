n = int(input())
A = list(map(int, input().split()))
# テレポート的なやつ
ans = []

for i in range(n):
    x = i+1
    j = 1
    while i+1 != A[x-1]:
        x = A[x-1]
        j += 1
    ans.append(j)
print(*ans)
