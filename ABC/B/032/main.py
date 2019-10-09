s = input()
k = int(input())
# if len(s) < k:
#     print(0)
# else:
#     print(len(set(s[i:i+k] for i in range(len(s)-k+1))))

# range()の中身は負になって、rangeは何も返さないけど、
# 空のset()の長さは0だから、ifなくても問題ない
print(len(set(s[i:i+k] for i in range(len(s)-k+1))))
