# ABC061 A - Between Two Integers
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def main():
    a, b, c = map(int, input().split())
    print('Yes' if a <= c <= b else 'No')


if __name__ == "__main__":
    main()
