n, r = map(int, input().split())
s = list(input())[::-1]
i = 0
fire = []
while '.' in s:
    if s[i] == '.':
        for j in range(i, i+r):
            if n <= j:
                continue
            s[j] = 'o'
        fire.append(max(0, n-1-j))
    i += 1
if fire:
    print(fire[0]+len(fire))
else:
    print(0)
