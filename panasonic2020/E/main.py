a = input()
b = input()
c = input()
ans = sum(map(len, [a, b, c]))
n = len(b) + len(c)
line = [[""]]*n+[[c]for c in a]+[[""]]*n
# print(line)

for i in range(len(line)-len(b)+1):
    print(line[i])
    line[i]

    # # i番目から、bを配置してみる
    # for j in range(len(line)-len(c)+1):
    #     # j番目からcを配置する
    #     # print(line[j])
    #     if
    #     pass
    ans = min(ans, x)

print(ans)
