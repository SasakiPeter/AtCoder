n = int(input())
*a, = map(int, input().split())

d, m = divmod(sum(a), n)
if m != 0:
    print(-1)
else:
    # print(d, "人になるように橋をかける")
    ans = 0
    cnt = 1
    prev = 0
    for n_people in a:
        if prev + n_people == d*cnt:
            ans += cnt - 1
            cnt = 1
            prev = 0
        else:
            prev += n_people
            cnt += 1
    print(ans)
