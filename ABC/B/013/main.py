a, b = [int(input()) for _ in range(2)]
print(min(abs(a-b), abs(abs(a-b)-10)))
# print(min(abs(a-b), 10-abs(a-b)))
