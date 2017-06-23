import os

for d in os.listdir('/'):
    print(d)
L = ["Hello", "Bobo", "HHHH", 66]
j = [i.lower() for i in L if isinstance(i, str)]
print(j)
g = (x * x for x in range(100))
for n in g:
    print(n)
