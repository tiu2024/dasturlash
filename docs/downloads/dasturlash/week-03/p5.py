x, y, z = input("Amal: ").split()

x = float(x)
z = float(z)

if y == '+':
    print("Natjia:", x + z)
elif y == "-":
    print("Natija:", x - z)
elif y == "*":
        print("Natija:", x * z)
elif y == "/":
    if z == 0:
        print("O ga bolb bolmaydi!")
    else:
        print("Natija:", x / z)
else:
    print("Bunday amal yoq!")