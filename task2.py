array = [1, 2, 3, 44, 43, 7, 77, 42, 5, 10, 11, 14]
result = []
for i, x in enumerate(array):
    if x % 7 == 0:
        result.append((x, i))
        

print(result)
