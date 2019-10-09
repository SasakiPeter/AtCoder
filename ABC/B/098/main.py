n = int(input())
s = input()
# 全探索可能
print(max(len(set(s[:i]) & set(s[i:])) for i in range(n)))
