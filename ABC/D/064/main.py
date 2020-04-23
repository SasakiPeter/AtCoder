n = int(input())
s = input()
need_L = 0
cnt = 0
for c in s:
    if c == ')':
        cnt += 1
        if 0 < cnt:
            need_L += 1
            cnt -= 1
    elif c == '(':
        cnt -= 1
need_R = max(-cnt, 0)
# print(cnt)
print('('*need_L+s+')'*need_R)
