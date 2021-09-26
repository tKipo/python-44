a = input()
x = len(a)
summ = 0
i = 0
while x > 0:
    summ = summ + int(a[i])
    i += 1
    x -= 1
print(summ)
