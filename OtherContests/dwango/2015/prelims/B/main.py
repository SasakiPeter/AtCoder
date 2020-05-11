import re
# r'\d'これも任意の数字
s = re.sub(r'[0-9]', ' ', input().replace('25', 'X'))
print(sum(c*(c+1)//2 for c in map(len, s.split())))


# import re
# s = input().replace('25', 'X')
# s = re.sub(r"[0123456789]", " ", s)
# ans = 0
# for c in map(len, s.split()):
#     ans += c*(c+1)//2
# print(ans)
