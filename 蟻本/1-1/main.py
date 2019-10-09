n, m = [int(input()) for _ in range(2)]
k = input().split()
lss = set()
# セット型を使えば、うまくnH4の計算量で行けそう n+3C4 O(n**4)
for w in k:
    for x in k:
        for y in k:
            for z in k:
                # ここで普通に全部足してフラグ立てた方が早くね
                lss |= {''.join(sorted(w+x+y+z))}
# 4回行う 復元抽出　3H4  6C2 6*5/2 15通り
print('Yes' if any(sum(map(int, s)) == m for s in lss) else 'No')
