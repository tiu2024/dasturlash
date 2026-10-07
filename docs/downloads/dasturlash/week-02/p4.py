def salom(ism = "Dostlarga"):

    ism = ism.title()

    print(f"Salom, {ism}")

def main():
    ism1 = input("Isming nma? ")
    salom(ism1)

    ism2 = input("Isming nma? ")
    salom(ism2)

main()