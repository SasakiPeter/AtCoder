n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
# x>=sum(m)+a*min(m) を満たす最大のa + n
print((x-sum(m))//min(m)+n)
