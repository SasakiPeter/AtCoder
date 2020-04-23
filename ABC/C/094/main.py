n = int(input())
X = list(map(int, input().split()))
sorted_X = sorted(X)
R = sorted_X[n//2]
L = sorted_X[n//2-1]
for x in X:
    print(R if x <= L else L)


# n = int(input())
# X = list(map(int, input().split()))

# # 中央の２数を取り出す
# # その小さい方の数字よりも小さいなら大きい方
# # 大きいなら、小さい方の数字を出力する
# larger_idx = n//2
# smaller_idx = larger_idx-1
# sorted_X = sorted(X)
# for x in X:
#     if x <= sorted_X[smaller_idx]:
#         print(sorted_X[larger_idx])
#     else:
#         print(sorted_X[smaller_idx])
