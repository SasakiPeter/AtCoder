s = list(input())

while s:
    s.pop()
    s.pop()
    n = len(s)
    if s[:n//2] == s[n//2:]:
        print(n)
        break

