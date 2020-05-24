import numpy as np
R, C, D = map(int, input().split())
A = np.array([input().split() for _ in range(R)], dtype=np.int16)
dist = np.arange(R)[:, None] + np.arange(C)[None, :]
select = (dist % 2 == D % 2) & (dist <= D)
answer = A[select].max()
print(answer)
