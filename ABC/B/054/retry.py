n, m = map(int, input().split())
# a = [list(input()) for _ in range(n)]
# b = [list(input()) for _ in range(m)]


class Image:
    def __init__(self, n):
        self.matrix = [list(input()) for _ in range(n)]
        self.n = n

    def isIncluded(self, a):
        for i in range(a.n-self.n+1):
            for j in range(a.n-self.n+1):
                template = [row[j:j+self.n] for row in a.matrix[i:i+self.n]]
                # print(template)

                if template == self.matrix:
                    return True
                # if a.matrix[i][j] == self.matrix[0][0]:
                #     # 重なる要素を取り出して、同じかを比べればいい
                #     if j+self.n <= a.n and i+self.n <= a.n:
                #         template = [a.matrix[i+k][j:j+self.n]
                #                     for k in range(self.n)]
                #         print(template)
                #         if template == self.matrix:
                #             return True
        return False


a = Image(n)
b = Image(m)

print("Yes" if b.isIncluded(a) else "No")
