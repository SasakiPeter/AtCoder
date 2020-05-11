# 増加して、減少する最も長い区間は？
n = int(input())
ans = 0
L = 0
prev = 0
is_increment = 1
for R in range(n):
    h = int(input())
    if prev < h:
        if not is_increment:
            is_increment = 1
            L = R-1
        else:
            ans = max(ans, R-L+1)
    elif prev > h:
        is_increment = 0
        ans = max(ans, R-L+1)
    # print(h, L, R, ans)
    prev = h
print(ans)
