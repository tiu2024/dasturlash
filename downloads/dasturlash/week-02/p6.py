def kvadrat(x):
    return x ** 2


def main():
    butun_son = int(input("Butun son: "))
    kasr_son = float(input("Kasr son: "))

    print(f"{butun_son} ning kvadrati = {kvadrat(butun_son)}")
    print(f"{kasr_son} ning kvadrati = {kvadrat(kasr_son)}")


main()
