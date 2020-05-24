n = int(input())
cnt = [0]*(n+1)
cnt[0] = 1
ans = None
for _ in range(n):
    a = int(input())
    if cnt[a] == 0:
        cnt[a] += 1
    else:
        ans = a
if ans is None:
    print('Correct')
else:
    print(ans, cnt.index(0))
