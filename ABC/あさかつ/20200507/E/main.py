n = int(input())
A = [int(input())for _ in range(n)]
A.extend(A)
max_cnt_zero = max_cnt_one = cnt = 0
# max_cnt = 0
cnt = 1
prev = -1
for a in A:
    if prev == a:
        cnt += 1
    else:
        # print(cnt, max_cnt, a)
        # max_cnt = max(max_cnt, cnt)
        if a == 0:
            max_cnt_zero = max(max_cnt_zero, cnt)
        else:
            max_cnt_one = max(max_cnt_one, cnt)
        cnt = 1
    prev = a
# print(max_cnt_one, max_cnt_zero)
max_cnt = max(max_cnt_one, max_cnt_zero)
# print(max_cnt_zero, max_cnt_one)

if 0 in (max_cnt_one, max_cnt_zero):
    print(-1)
else:
    print((max_cnt-1)//2+1)
# print(max_cnt)
