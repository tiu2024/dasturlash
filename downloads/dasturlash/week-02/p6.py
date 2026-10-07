def kvadrat(x):
    return x ** 2

def main():

    iraqam = int(input("Butun son: "))
    fraqam = float(input("Kasr son: "))

    print(f"Butun {iraqam} son kvadrati = {kvadrat(iraqam)}")
    print(f"Kasr {fraqam} son kvadrati = {kvadrat(fraqam)}")

main()