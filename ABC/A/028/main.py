n = int(input())
print('Perfect' if n == 100 else 'Bad' if n <
      60 else 'Good' if 60 <= n < 90 else 'Great')

# if つかわないパターン
# print((['Bad']*6+['Good']*3+['Great']+['Perfect'])[n//10])
