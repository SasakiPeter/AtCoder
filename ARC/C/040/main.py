n = int(input())
FIELD = [['o']*(n+2)]
for _ in range(n):
    FIELD.append(list('o'+input()+'o'))
else:
    FIELD.append(['o']*(n+2))

ans = 0
for i in range(1, n+1):
    # ここ、文字列ならrfindが使える
    # でも、書き換えるのが下手くそなので、微妙
    for j in reversed(range(1, n+1)):
        if FIELD[i][j] == '.':
            ans += 1
            # きれいに塗る必要はない
            # 行の一番最後の.までぬる
            for k in range(j, n+1):
                FIELD[i+1][k] = 'o'
            break

            # きれいに塗ると、効率悪い
            # for k in range(j, n+1):
            #     FIELD[i][k] = 'o'
            #     if FIELD[i][k+1] == 'o':
            #         break
            # for l in range(k, n+1):
            #     FIELD[i+1][l] = 'o'
            #     if FIELD[i+1][l+1] == 'o':
            #         break

print(ans)
