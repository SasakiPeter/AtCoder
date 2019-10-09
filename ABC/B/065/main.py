n = int(input())
a = [int(input()) for _ in range(n)]

x = a[0]
for i in range(n):
    if x == 2:
        print(i+1)
        break
    x = a[x-1]
else:
    print(-1)

# こんなんあるらしいけど、上の方が良さそう
# n=int(input())
# a=[int(input()) for i in range(n)]
# c,s=1,a[0]
# while s!=2 and c<n:c,s=c+1,a[s-1]
# print(c if c<n else -1)
