a = int(input())
b = a // 100
c = (a - b * 100) // 10
d = a - b * 100 - c * 10
print(b + c + d)
