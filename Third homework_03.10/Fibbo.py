a = 0
b = 1


def fibb(n):
    while n > 0:
        global a, b
        a, b = b, a + b
        n -= 1
        yield a


val = fibb(10)
for x in val:
    print(x)
