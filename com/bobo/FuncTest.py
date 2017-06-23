from functools import reduce

f = abs


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


def f(x):
    return x * x


st = [1, 2, 3, 4, 5, 6, 7]


def f(x, y):
    return x + y


i = reduce(f, [1, 3, 5, 7, 9], 100)
print(i)
print(map(str, st))
print(st)


def isOld(n):
    return n % 2 == 1


iterator = filter(isOld, [1, 2, 3, 4, 6, 7])
for i in iterator:
    print(i)


def notEmp(st):
    return st and st.strip() and str(st).replace(" ", "1")


l = [" AA  ", "", None, "BB "]
filter1 = filter(notEmp, l)
print(l)
print(tuple(filter1))

print(sorted({"1": "yi", "6": "jiu", "3": "san"}))


def comv(x, y):
    if x > y:
        return 1
    else:
        return -1


sorted1 = sorted([4, 7, 8, 1, 88, 2], key=lambda s: [2])
print(sorted1)


def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax += i
        return ax

    return sum


map1 = list(map(lambda x: x * x, [1, 2, 3, 4]))
print(map1)

f = lambda *x: print(x)
f(*[1, 2, 3, 4])
