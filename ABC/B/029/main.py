# s = [input() for _ in range(12)]
# print(sum(1 if 'r' in x else 0 for x in s))

# 923 lenがO(1)と知っている今なら
print(len([1 for _ in range(12) if 'r' in input()]))
