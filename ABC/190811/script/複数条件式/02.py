import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def main():
    a, b, x = map(int, input().split())
    # print('YES' if x <= a+b and a <= x else 'NO')
    print('YES' if a <= x <= a+b else 'NO')


if __name__ == "__main__":
    main()
