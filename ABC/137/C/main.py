from collections import Counter
n = int(input())
s = [''.join(sorted(input())) for _ in range(n)]
d = Counter(s)
print(sum(v*(v-1)//2 for v in d.values()))

# from collections import Counter
# print(sum(v*(v-1)//2 for v in Counter(''.join(sorted(input())) for _ in range(int(input()))).values()))

# この場合はcountメソッドは使えなさそう
