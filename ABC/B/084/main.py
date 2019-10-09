a, b = map(int, input().split())
s = input()
print('Yes' if len(s) == a + b + 1 and s[a] == '-'
      and all(i in '0123456789' for i in s[:a]+s[a+1:]) else 'No')

# 数字であることは確約されていた
# さらにsはa+b+1であった
print('Yes' if s.count('-') == 1 and s[a] == '-' else 'No')

# ちゃんと制約を読みましょう！
