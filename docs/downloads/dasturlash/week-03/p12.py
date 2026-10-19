a, amal, b = input("Amal: ").split()

a = float(a)
b = float(b)

if amal == "+":
    print("Natija:", a + b)
elif amal == "-":
    print("Natija:", a - b)
elif amal == "*":
    print("Natija:", a * b)
elif amal == "/":
    if b == 0:
        print("0 ga bo'lib bo'lmaydi!")
    else:
        print("Natija:", a / b)
else:
    print("Bunday amal yo'q!")
