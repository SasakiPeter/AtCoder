n = int(input())
*l_list, longest = sorted(map(int, input().split()))
print('Yes' if longest < sum(l_list) else 'No')
