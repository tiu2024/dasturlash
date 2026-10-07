def main():
    vaht = input("Soat nechida boldi? ")

    vaht = convert(vaht)

    if vaht >= 7.0 and vaht <= 8.0:
        print("Nonushta vaqti!")
    elif vaht >= 12.0 and vaht < 13.0:
        print("Tushlik vaqti!")
    elif vaht >= 18.0 and vaht < 19.0:
        print("Kechki ovqat vaqti!")
    else:
        print("Ishlaymiz!")

def convert(vaht):
    soat, minut = vaht.split(":")

    return float(soat) + (float(minut) / 60)

main()