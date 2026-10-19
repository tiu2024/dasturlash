import string


def salom(ism="Do'stlarga"):
    ism = string.capwords(ism)
    print(f"Salom, {ism}")


def main():
    ism1 = input("Ismingiz nima? ")
    salom(ism1)

    ism2 = input("Ismingiz nima? ")
    salom(ism2)


main()
