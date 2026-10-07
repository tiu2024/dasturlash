def main():
    narh = narh_to(input("Qancha boldi? "))
    foiz = foiz_to(input("Nechi foiz? "))

    tip = narh * foiz

    print(f"Tip: {tip:.2f}")



def narh_to(n):

    n = n.strip("$")

    return float(n)

def foiz_to(f):

    f = f.strip("%")

    return float(f) / 100


main()
