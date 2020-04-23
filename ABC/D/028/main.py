n, k = map(int, input().split())
# 1<= rand <= n
ans = 0

# 全部Kの個数
ans += 1

# １つだけKでない個数 n, k = 3, 2 で 221 とか　223とか
ans += (n - 1)*3

# 全部違うものの個数
large = n - k
small = k - 1
ans += (large*small)*2*3

print(ans/(n**3))
