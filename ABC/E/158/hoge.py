import time
start = time.time()
int("9"*2*(10**5)) % 3
end = time.time() - start
print(end*10**3, 'ms')

start = time.time()
int("1"+"0"*2*(10**5)) % 3
end = time.time() - start
print(end*10**3, 'ms')

start = time.time()
int("1"+"0"*2*(10**5))
end = time.time() - start
print(end*10**3, 'ms')

start = time.time()
10**(2*10**5) % 3
end = time.time() - start
print(end*10**3, 'ms')

start = time.time()
pow(10, (2*10**5), 3)
end = time.time() - start
print(end*10**3, 'ms')
