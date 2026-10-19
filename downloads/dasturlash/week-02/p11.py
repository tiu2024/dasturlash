def main():
    narx = narxga_aylantir(input("Qancha bo'ldi? "))
    foiz = foizga_aylantir(input("Necha foiz? "))

    tip = narx * foiz

    print(f"Tip: {tip:.2f}")


def narxga_aylantir(n):
    n = n.strip("$")
    return float(n)


def foizga_aylantir(f):
    f = f.strip("%")
    return float(f) / 100


main()
