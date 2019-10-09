# from decimal import Decimal

# p = Decimal(input())
# ans = p+1
# cnt = 0
# while True:
#     t = Decimal(cnt) + p/Decimal((2**(cnt/1.5)))
#     if ans > t:
#         ans = t
#     else:
#         break
#     cnt += 0.001
# print(ans)

# scipy.optimizeで関数の出力を最適化するのが吉
from scipy.optimize import fmin, brent
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

p = float(input())


def f(t):
    # if t < 0:
    #     return p+1
    # return t + p/(2**(t/1.5))
    return max(0, t) + p/(2**(t/1.5))


# この記述だと、２回関数に突っ込んでて効率悪い
# xoptだけじゃなくて、yoptも一緒に取得すべき
# xopt = fmin(f, 0, xtol=1e-10, disp=False)
# formatで桁数を合わせれば、テストケースで検証できる
# print('{:.10f}'.format(f(xopt[0])))

# full_outputにしないと、探索した最小のxしか返してくれない
xopt, fopt, *_ = fmin(f, 0, xtol=1e-10, full_output=True, disp=False)
print('{:.10f}'.format(fopt))


# print(brent(f, full_output=True))

# for i in range(int(p)+1):
#     print(f(i))
#     if i > 100:
#         break
