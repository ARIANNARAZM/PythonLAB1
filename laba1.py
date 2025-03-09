x = int(input("Введите x: "))
y = int(input("Введите y: "))

if (x * y) > 0:
    print("a =", (x**2 + y)**2 - (x**2*y)**0.5)
elif (x * y) < 0:
    print("a =", (x**2 + y)**2 + (abs(x**2*y))**0.5)
elif (x * y) == 0:
    print("a =", (x**2 + y)**2 +1)