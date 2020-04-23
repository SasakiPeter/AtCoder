txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())

uwaki = False

for _ in range(n):
    x, y = map(int, input().split())
    # 誰か一人の家にでもよったら、アウト
    a = ((txa - x)**2 + (tya - y)**2)**.5
    b = ((txb - x)**2 + (tyb - y)**2)**.5
    if (a+b) <= T*V:
        uwaki = True
        break


print('YES' if uwaki else 'NO')
