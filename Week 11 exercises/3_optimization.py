import time


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


memo = dict()


def nfib(n):
    if n in memo.keys():
        return memo.get(n)
    elif n < 2:
        return 1
    else:
        memo[n] = nfib(n - 1) + nfib(n - 2)
    return memo[n]


start = time.time()
print(fib(32))  # adjust the argument as needed to take 1 second
print(f'Time for fib: {time.time() - start}')
start = time.time()
print(nfib(32))  # adjust the argument as needed to take 1 second
print(f'Time for nfib: {time.time() - start}')
