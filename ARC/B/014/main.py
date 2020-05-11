n = int(input())
history = set()
prev = ""
takahashi_win = 0
for i in range(n):
    w = input()
    if not prev:
        prev = w
        history.add(w)
        continue

    if prev[-1] == w[0] and w not in history:
        prev = w
        history.add(w)
    else:
        if i % 2 != 0:
            takahashi_win = 1
        break
else:
    print('DRAW')
    exit()

if takahashi_win:
    print('WIN')
else:
    print('LOSE')
