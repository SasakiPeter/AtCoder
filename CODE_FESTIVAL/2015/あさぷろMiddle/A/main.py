N, K, M, R = map(int, input().split())
S = sorted([int(input()) for _ in range(N-1)], reverse=True)

if R*K <= sum(S[:K]):
    print(0)
else:
    ans = R*K-sum(S[:K-1])
    if ans <= M:
        print(ans)
    else:
        print(-1)
