def is_prime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
    return True

def get_prime_list(n1=0,n=10000):
    a = []
    for i in range(n1, n+1):
        a.append(i)
    a[1] = 0
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    return lst


def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            # print(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
        # print(n)
    return Ans




def fib(n=100):
    f = [0,1]
    while len(f) <= n:
        new_fibo = f[-1] + f[-2]
        f.append(new_fibo)
    return f
