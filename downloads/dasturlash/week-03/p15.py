import string


def main():
    toliq_ism = string.capwords(input("Ism va familiyangiz? "))

    print(f"Salom, {ism_ajratish(toliq_ism)}")


def ism_ajratish(toliq_ism):
    birinchi, ikkinchi = toliq_ism.split()

    if birinchi.endswith("ov") or birinchi.endswith("ova"):
        return ikkinchi

    return birinchi


main()
