n = int(input())
A = [(a, i+1) for i, a in enumerate(map(int, input().split()))]
A.sort(reverse=True)
for _, i in A:
    print(i)
