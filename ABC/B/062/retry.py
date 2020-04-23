h, w = map(int, input().split())
print('#'*(w+2))
print(*['#'+input()+'#' for _ in range(h)], sep='\n')
print('#'*(w+2))
