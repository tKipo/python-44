a = input()
b = input()
if a.isdigit() and b.isdigit() is True:
    a = float(a)
    b = float(b)
    if 3 <= a <= 23 and 3 <= b <= 23:
        print(abs(a - b))
    else:
        print(a + b)
else:
    print(a + b)
