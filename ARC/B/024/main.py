n = int(input())
A = [int(input())for _ in range(n)]
# 循環しているので2N回す
# 最長の連続を探す
A.extend(A)

prev = 0
max_zero_cnt = 0
max_one_cnt = 0
cnt = 0

for c in A:
    if c == prev:
        cnt += 1
    else:
        if c:
            max_zero_cnt = max(max_zero_cnt, cnt)
        else:
            max_one_cnt = max(max_one_cnt, cnt)
        prev = c
        cnt = 1

max_chain = max(max_one_cnt, max_zero_cnt)
if max_chain:
    print((max_chain-1)//2+1)
else:
    print(-1)
