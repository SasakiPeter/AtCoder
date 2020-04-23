n = int(input())
MAX = 0
longest = 0
# D = []
for _ in range(n):
    d = int(input())
    # D.append(d)
    MAX += d
    longest = max(longest, d)

# INF = 10**5
# MIN = INF
# for d in D:
#     print(0 if 2*d <= MAX else 2*d - MAX)
#     MIN = min(0 if 2*d <= MAX else 2*d - MAX, MIN)

# if longest <= MAX - longest:
#     MIN = 0
# else:
#     MIN = 2*longest - MAX

MIN = 0 if 2*longest <= MAX else 2*longest - MAX

print(MAX)
print(MIN)
