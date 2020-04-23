N = int(input())
F = [int(input().replace(" ", ''), 2) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

outcome_list = []
for i in range(1, 1 << 10):
    outcome = 0
    for f, p in zip(F, P):
        # both = "{:010b}".format(i & f)
        # n_store = sum(map(int, list(both)))
        n_store = "{:010b}".format(i & f).count("1")
        outcome += p[n_store]
    outcome_list.append(outcome)
print(max(outcome_list))

# 結構頑張って、いい感じにできた！
# n = int(input())
# # f = ["0b"+input().replace(" ", '') for _ in range(n)]
# f = [input().replace(" ", '') for _ in range(n)]
# p = [list(map(int, input().split())) for _ in range(n)]

# outcome_list = []
# for i in range(1, 1 << 10):
#     # x = bin(i)
#     # print(list(map(int, x[2:])))
#     # print(list("{:10b}".format(i)))
#     # joisino = list(map(int, "{:010b}".format(i)))
#     # joisino = "{:#012b}".format(i)

#     # joisino = "{:010b}".format(i)
#     outcome = 0
#     for j, x in enumerate(f):
#         # 0b付けないで、int(num, 2)でもいいかも
#         # num = int(joisino, 0) & int(x, 0)
#         # both = "{:010b}".format(int(joisino, 2) & int(x, 2))
#         both = "{:010b}".format(i & int(x, 2))
#         # print(joisino, x)
#         n_store = sum(map(int, list(both)))
#         outcome += p[j][n_store]
#     outcome_list.append(outcome)
# print(max(outcome_list))
