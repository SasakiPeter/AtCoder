n, k, c = map(int, input().split())
s = input()

ans = []
for i in range(n):
    # 範囲で区切って、その中に一個しかoがないゾーンがあったらビンゴ

    # if s[i:i+c].count("o") == 1:
    idx_ls = []
    for j in range(c):
        if i+j < n:
            if s[i+j] == 'o':
                idx_ls.append(i+j)
    if len(idx_ls) == 1:
        ans.append(idx_ls[0]+1)


print(*ans, sep='\n')
