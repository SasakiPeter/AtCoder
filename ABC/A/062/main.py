# s = set(map(int, input().split()))
# b, c = {4, 6, 9, 11}, {2}
# a = {i for i in range(1, 13)}-b-c
# print('Yes' if any(x & s == s for x in (a, b, c)) else 'No')

# IQ200戦略
# s = 'XACABABAABABA'
# x, y = map(int, input().split())
# print('Yes' if s[x] == s[y] else 'No')

# 923
# a = {1, 3, 5, 7, 8, 10, 12}
# b = {4, 6, 9, 11}
# c = {2}
# d = set(map(int, input().split()))
# print('Yes' if d <= a or d <= b or d <= c else 'No')

a = [{1, 3, 5, 7, 8, 10, 12}, {4, 6, 9, 11}, {2}]
s = set(map(int, input().split()))
print('Yes' if any(s <= x for x in a) else 'No')
