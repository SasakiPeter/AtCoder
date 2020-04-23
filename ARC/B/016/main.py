n = int(input())
SCORE = [list(input()) for _ in range(n)]
ans = 0

for notes in zip(*SCORE):
    long_notes = 0
    for note in notes:
        long_notes ^= note != 'o' and long_notes
        if note == '.':
            continue
        if note == 'x':
            ans += 1
        if note == 'o' and not long_notes:
            long_notes ^= 1
            ans += 1

print(ans)
