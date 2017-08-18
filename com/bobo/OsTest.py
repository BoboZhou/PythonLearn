def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f = count()
for i in f:
    print(i())

i, j, k = [1, 2, 3]


def bulid(x, y):
    return lambda: x * x + y * y


print(bulid(1, 2)())
