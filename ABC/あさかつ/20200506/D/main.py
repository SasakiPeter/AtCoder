n = int(input())
d_ls = [int(input()) for _ in range(n)]
*ds, max_d = sorted(d_ls)
print(sum(d_ls))
print(max(0, max_d-sum(ds)))
