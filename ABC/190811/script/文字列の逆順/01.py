# ABC077 A - Rotation

# pot
# top

a, b = [input() for _ in range(2)]
print('YES' if a == b[::-1] else "NO")
print('YES' if a == reversed(b) else "NO")
print(*reversed(b), ''.join(reversed(b)), b[::-1])
