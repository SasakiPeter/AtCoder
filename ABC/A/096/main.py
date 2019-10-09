a, b = map(int, input().split())
# print([a-1, a][a <= b])
# print([a, a-1][a > b])

# これでいい
print(a-(a > b))
