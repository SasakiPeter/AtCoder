T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = sorted(map(int, input().split()))

if n < m:
    print('no')
    exit()

takoyaki = [0]*(101)

for a in A:
    takoyaki[a] += 1

# どこのindexまでみたか管理してあげると、もっと高速にできるかも
for b in B:
    for t in range(T, -1, -1):
        if b-t < 0:
            continue
        if takoyaki[b-t] > 0:
            takoyaki[b-t] -= 1
            break
    else:
        print("no")
        exit()
else:
    print("yes")

# print(dp)

# print("yes" if all(0 <= x for x in dp) else "no")
