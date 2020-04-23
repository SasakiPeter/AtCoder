n, k = map(int, input().split())
# print(n, k)
MOD = 10**9+7
ans = 0
for i in range(k, n+1):
    # i個えらぶ 0~iまでの和~

    # cnt = (2*n-k+1)*(k-1)//2 - i*i//2 + 1
    cnt = (2*n-i+1)*i // 2 - (i-1)*i//2 + 1
    ans = ans + cnt % MOD
print(ans % MOD + 1)
