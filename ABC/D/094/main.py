n = int(input())
ax, *A = sorted(map(int, input().split()), reverse=True)
median = ax/2
mid = A[0]
for a in A[1:]:
    if abs(median-mid) > abs(median-a):
        mid = a

print(ax, mid)
