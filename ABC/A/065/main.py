x, a, b = map(int, input().split())
print('delicious' if a-b >= 0 else 'safe' if a-b+x >= 0 else 'dangerous')
