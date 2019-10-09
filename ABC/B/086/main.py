# a, b = input().split()
# n = int(a+b)
# print('Yes' if int(n**.5)**2 == n else 'No')

n = int(input().replace(' ', ''))
# print('Yes' if n**.5 % 1 == 0 else 'No')
# あまりがない時は0でFalse扱い
print('No' if n**.5 % 1 else 'Yes')
