import math
a = float(input("Длина первой стороны треугольника: "))
b = float(input("Длина второй стороны треугольника: "))
alpha = float(input("Угол между этими сторонами (в градусах): "))
alpha = math.degrees(alpha)

c_squared = a**2 + b**2 - a*b*math.cos(alpha)
print('Длина третьей стороны: ', math.sqrt(c_squared))