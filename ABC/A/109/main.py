# a, b = map(int, input().split())
# print('Yes' if a*b % 2 and a*b*3 % 2 else 'No')

# こんなことしなくても、これでええやん
# print('No' if '2' in input() else 'Yes')

# こういうのもある
print('Yes' if eval(input().replace(' ', '*')) % 2 else 'No')
