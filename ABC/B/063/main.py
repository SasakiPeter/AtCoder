s = input()
# print('yes' if len(s) == len(set(s)) else 'no')

# 頭良さそう
print('no' if len(s) - len(set(s)) else 'yes')
