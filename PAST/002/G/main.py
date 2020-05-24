from collections import defaultdict, deque


s = deque([])
q = int(input())
for _ in range(q):
    com, *query = input().split()
    if com == '1':
        c, x = query
        s.append((c, int(x)))
    else:
        d = int(query[0])
        del_cnt = defaultdict(int)
        cnt = 0
        while s and cnt != d:
            c, x = s.popleft()
            if d <= cnt+x:
                ret = x-(d-cnt)
                if ret:
                    s.appendleft((c, ret))
                del_cnt[c] += d-cnt
                cnt += d-cnt
            else:
                cnt += x
                del_cnt[c] += x
        print(sum(v**2 for v in del_cnt.values()))
