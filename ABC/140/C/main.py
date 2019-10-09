n = int(input())
B = list(map(int, input().split()))
# len(B)よりnじゃね？
# print(B[0]+B[-1] + sum(min(B[i], B[i+1])for i in range(len(B)-1)))

# pythonistaならindex参照でなくzipを使いこなせ！！
print(B[0]+B[-1] + sum(min(x, y) for x, y in zip(B, B[1:])))
