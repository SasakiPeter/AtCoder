n, m = map(int, input().split())
divisors = set()
for i in range(1, int(m**.5)+1):
    if m % i == 0:
        divisors |= {i, m//i}
divisors = sorted(divisors)
for div in divisors:
    if n <= div:
        print(m//div)
        break
