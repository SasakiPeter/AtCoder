n = int(input().replace(' ', ''))
# 偶数indexの文字列のみ取得するという方法もある
# n = int(input()[::2])
print('NO' if n % 4 else 'YES')
