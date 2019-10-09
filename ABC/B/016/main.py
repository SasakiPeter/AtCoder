a, b, c = map(int, input().split())
print('?' if a+b == a-b == c else '+' if a +
      b == c else '-' if a-b == c else '!')
