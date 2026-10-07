a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))

if a >= b and a >= c:
    print("Eng kattasi:", a)
elif b >= c:
    print("Eng kattasi:", b)
else:
    print("Eng kattasi:", c)
