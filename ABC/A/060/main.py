s = input().split()
# n個でもOK
print('YES' if all(s[i][-1] == s[i+1][0] for i in range(len(s)-1)) else 'NO')
