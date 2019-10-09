a, b = map(int, input().split())
# タップの数は1 + (a-1)*n >= b
print(-(-(b-1)//(a-1)))
