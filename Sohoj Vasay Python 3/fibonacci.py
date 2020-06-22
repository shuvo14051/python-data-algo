def fib(n):
    a,b = 0, 1
    series = []
    while b<n:
        series.append(b)
        a,b = b,a+b
    return series

if __name__ == '__main__':
    print(fib(100))