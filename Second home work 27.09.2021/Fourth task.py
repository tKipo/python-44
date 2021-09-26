import math
rectangle_triangle_circle = input('''Если считаем площадь прямоугольника - введите r  
Если считаем площадь треугольника - введите t  
Если считаем площадь круга - введите c\n''')
if rectangle_triangle_circle == "r":
    a = float(input('Введите длину: '))
    b = float(input('Введите ширину: '))
    print(a * b)
elif rectangle_triangle_circle == "t":
    a = float(input('Введите длину первой сторны: '))
    b = float(input('Введите длину второй сторны: '))
    c = float(input('Введите длину третьей сторны: '))
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
elif rectangle_triangle_circle == "c":
    r = float(input('Введите радиус: '))
    print(3.14 * (r ** 2))
