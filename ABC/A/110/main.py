# s = list(map(int, input().split()))
# print(max(s)*10+sum(s)-max(s))

# ソートが発想できなかった　つらい
# a, b, c = sorted(map(int, input().split()))
# print(a+b+c*10)

# これはきもい
print(eval('+'.join(sorted(input()))+'*10'))
