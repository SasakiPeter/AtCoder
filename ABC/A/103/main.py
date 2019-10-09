# a, b, c = sorted(map(int, input().split()))
# print(c-a)

# max min とsortは紙一重

# import time
# start = time.time()

# これかっこいい
*a, = map(int, input().split())
# ls = list(map(int, input().split()))

print(max(a) - min(a))


# end = time.time() - start
# print(end*10**3, 'ms')
