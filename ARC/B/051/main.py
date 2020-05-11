k = int(input())
# k = 40
dp = [0]*(k+1)
dp[0] = 1
dp[1] = 3
for i in range(2, k+1):
    dp[i] = dp[i-2]+dp[i-1]
# print(dp[-1], dp[-2])
print(dp[k], dp[k-1])

# cnt = 0


# def gcd(a, b):
#     global cnt
#     if b == 0:
#         return a
#     cnt += 1
#     # print(a, b, is_prime(a), is_prime(b))
#     return gcd(b, a % b)


# gcd(dp[-1], dp[-2])
# assert cnt == k
