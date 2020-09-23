import math
b = int(input("Длина первой стороны треугольника: "))
c = int(input("Длина второй стороны треугольника: "))
angle = int(input("Угол между этими сторонами: "))
a_squared = b**2 + c**2 - 2*b*c*math.cos(angle)
print("Длина третьей стороны: ", math.sqrt(a_squared))

