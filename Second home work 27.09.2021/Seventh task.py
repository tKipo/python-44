def bank(a, years):
    while years > 0:
        years -= 1
        a = a * 1.1
    print(int(a))


bank(1000, 1)
