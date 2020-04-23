N, L = map(int, input().split())
kuji = [input() for _ in range(L)][::-1]
start_idx = input().index('o')
max_idx = 2*N-2

line_idx = start_idx
for row in kuji:
    if 0 < line_idx:
        left = row[line_idx-1]
        if left == '-':
            line_idx -= 2
            continue
    if line_idx < max_idx:
        right = row[line_idx+1]
        if right == '-':
            line_idx += 2

ans = line_idx//2 + 1
print(ans)
