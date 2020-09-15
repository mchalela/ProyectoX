

def fib(n):
	'''documentacion'''
    values = [0, 1]
    while values[-2] < n:
        values.append(values[-2] + values[-1])
    return values


def prime(n):
	'''documentacion'''
    p = []
    for num in range(n+1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            p.append(num)
    print(n)
    return p