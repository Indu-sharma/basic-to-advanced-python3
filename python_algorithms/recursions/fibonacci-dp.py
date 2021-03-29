import datetime


def fib(myfunction):
    return myfunction


def iter_fib(n):
    first = 1
    second = 1
    if n == 1 or n == 2:
        return 1
    i = 3
    while i <= n:
        first, second = second, first + second
        i = i + 1
    return second


def rec_fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


mem_cache = {}


def rec_mem_fib(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    else:
        if n in mem_cache:
            value = mem_cache[n]
        else:
            value = rec_mem_fib(n - 1) + rec_mem_fib(n - 2)
            mem_cache[n] = value
    return value


def rec_mem1_fib(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    else:
        if n in mem_cache:
            value = mem_cache[n]
        else:
            value = rec_mem_fib(n - 1) + rec_mem_fib(n - 2)
            mem_cache[n] = value
    return value


def display(func, n):
    return fib(func(n))


def test(func):
    t1 = datetime.datetime.now()
    for i in range(1, 30):
        display(func, i)
    t2 = datetime.datetime.now()
    print("TimeTaken by Func: {} is {}".format(func.__name__, t2 - t1))


test(iter_fib)
test(rec_fib)
test(rec_mem_fib)

'''
Sample o/p:
TimeTaken by Func: iter_fib is 0:00:00.000313
TimeTaken by Func: rec_fib is 0:00:00.383503
TimeTaken by Func: rec_mem_fib is 0:00:00.000038
'''
