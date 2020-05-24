n = int(input())
A = [a-i-1 for i, a in enumerate(map(int, input().split()))]
# 中央値とる
if n & 1:
    mid = n//2
else:
    mid = (n-1)//2
median = sorted(A)[mid]
print(sum(map(lambda x: abs(x-median), A)))
