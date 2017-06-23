def fact(n, k):
    if n == 1:
        return k
    else:
        return fact(n - 1, n * k)


r = []
for i in range(3):
    r.append(i)

print(r[-1:])
l = range(100)

for i in l[:10:2]:
    print(i)

d = {"1": "yi", "2": "er", "3": "san"}
for i in d.values():
    print(i)

for i in d.keys():
    print(i)

for i in d.items():
    print(i)
    if i[0] == '1':
        print("get :", i[1])

for i, va in d.items():
    print(i, va)

for i, val in enumerate([3, 8, 2, 6]):
    print(i, val)
l = [x * 2 for x in range(11)]
print(l)

k = [x + 1 for x in range(11) if x > 5]
print(k)

h = [m + n for m in 'abc' for n in 'xyz']
print(h)
