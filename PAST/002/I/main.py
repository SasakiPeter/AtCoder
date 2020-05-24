n = int(input())
A = list(map(int, input().split()))
T_LEN = 1 << n
node = [(0, -1)]*(2*T_LEN)
INF = 10**18


def update(i, x):
    i += T_LEN
    node[i] = (x, i-T_LEN)
    while i > 0:
        i //= 2
        node[i] = sorted([node[i*2], node[i*2+1]])[1]


for i in range(T_LEN):
    update(i, A[i])


cnt = [0]*T_LEN
for _, i in node[2:]:
    cnt[i] += 1
for x in cnt:
    print(x)
