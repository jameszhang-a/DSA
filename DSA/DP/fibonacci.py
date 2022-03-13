from timeit import default_timer as timer

N = 30


def fib_recursive(n):
    if n == 1 or n == 0:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_slide(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return b


# also know as: top down
def fib_memo(n, dp={1: 1, 0: 1}):
    if n in dp:
        return dp[n]

    dp[n] = fib_memo(n - 1, dp) + fib_memo(n - 2, dp)
    return dp[n]


def fib_bottom(n):
    dp = [1, 1] + [None] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def pfib(fib, n):
    for i in range(n):
        print(fib(i))


def runtime(fib, n, iter=10):
    total_time = 0
    for _ in range(iter):
        start = timer()
        fib(n)
        end = timer()

        total_time += (end - start) * 1000

    per_trial = total_time / iter

    print(per_trial)


# pfib(fib_recursive, N)
# print()
# pfib(fib_slide, N)
# print()
# pfib(fib_memo, N)
# print()

# from worst to best
print("Naive:")
runtime(fib_recursive, N)

print("Bottom Up")
runtime(fib_bottom, N)

print("Memo")
runtime(fib_memo, N)

print("Slide: ")
runtime(fib_slide, N)
