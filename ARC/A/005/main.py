n = int(input())
s = input().rstrip('.').split()
takahashi = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']
print(sum(w in takahashi for w in s))

# これはずるい
# input()
# print(input()[:-1].lower().split().count('takahashikun'))
