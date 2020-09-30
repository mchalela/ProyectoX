

def fib(n):
    '''documentacion'''
    values = [0, 1]
    while (new := values[-2] + values[-1]) <= n:
        values.append(new)
    return values


def prime(n):
    '''documentacion'''
    p = []
    for num in range(1, n+1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            p.append(num)
    return p