# n = int(input())
# t, a = map(int, input().split())
# *h, = map(lambda x: abs(t-x*0.006-a), (map(int, input().split())))
# print(h.index(min(h))+1)

# 926
n = int(input())
t, a = map(int, input().split())
h = list(map(lambda x: abs(t-int(x)*.006-a), input().split()))
print(h.index(min(h))+1)
