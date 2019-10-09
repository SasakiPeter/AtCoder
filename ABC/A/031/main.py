a, d = map(int, input().split())
print(max((a+1)*d, a*(d+1)))

# なるほど回答
# print(a*d+max(a, d))
# print(max(a, d)*(min(a, d)+1))
