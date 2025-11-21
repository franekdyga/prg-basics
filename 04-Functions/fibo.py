def fibo(n):
    a = 1
    b = 1
    for i in range(n):
        print(a)
        b = b+a
        a = b-a


fibo(10)