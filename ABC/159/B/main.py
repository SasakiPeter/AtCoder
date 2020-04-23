s = input()
n = len(s)
cnt = 0
if s == s[::-1]:
    cnt += 1
# print(cnt)
idx = (n-1)//2
if s[:idx] == s[:idx][::-1]:
    cnt += 1
# print(cnt)
idx = (n+3)//2-1
# print(s[idx:])
if s[idx:] == s[idx:][::-1]:
    cnt += 1

# print(cnt)
print("Yes" if cnt == 3 else "No")
