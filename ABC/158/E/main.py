n, p = map(int, input().split())
s = input()

# MAX = int(s) // p
# for i in range(MAX):
#     print(i * p)


# 全探索なら
ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        print(s[i:j])
        ans += (int(s[i:j]) % p == 0) + 0
print(ans)
