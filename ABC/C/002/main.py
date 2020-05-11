# import numpy as np
# a, b, c = [np.array([x, y]) for x, y in zip(*[map(int, input().split())]*2)]
# # 誤差が小さい
# print(abs(np.cross(b-a, c-a))/2)
# # # 誤差が大きい
# # print(abs(np.linalg.det([b-a, c-a]))/2)


# class P:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __sub__(self, q):
#         return P(self.x-q.x, self.y-q.y)

#     def cross(self, q):
#         return self.x*q.y-self.y*q.x


class P:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __sub__(self, q):
        return P(self.x-q.x, self.y-q.y)

    def cross(self, q):
        return self.x*q.y-self.y*q.x


a, b, c = [P(x, y) for x, y in zip(*[map(int, input().split())]*2)]
print(abs((b-a).cross(c-a))/2)
