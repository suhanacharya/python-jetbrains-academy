def fibonacci(n):
    x, y = 0, 1
    i = 1
    while i <= n:
        yield x
        x, y = y, x + y
        i += 1
