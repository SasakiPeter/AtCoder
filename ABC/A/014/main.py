a, b = [int(input()) for _ in range(2)]
# a+m = b*n　を満たすようなaを求めて
print(b*(-(-a//b))-a)

# -7 % 3 は 2となる
# print(-a % b)
