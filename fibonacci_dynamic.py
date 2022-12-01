import sys


def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == '__main__':
    args = sys.argv[1:]
    print(fib(int(args[0])))
