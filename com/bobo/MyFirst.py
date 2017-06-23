def fact(n, k):
    if n == 1:
        return k
    else:
        return fact(n - 1, n * k)


print(fact(5, 1))
print(fact(5, 1))
