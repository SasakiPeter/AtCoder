a, b = map(int, input().split())
print('Impossible' if a % 3 and b % 3 and (a+b) % 3 else 'Possible')

# 条件としてandを使う場合は、*で表すことが可能
# print('Impossible' if a*b*(a+b) % 3 else 'Possible')
