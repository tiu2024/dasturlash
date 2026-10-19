def main():
    vaqt = input("Soat necha bo'ldi? ")

    vaqt = soatga_aylantir(vaqt)

    if vaqt >= 7.0 and vaqt <= 8.0:
        print("Nonushta vaqti!")
    elif vaqt >= 12.0 and vaqt <= 13.0:
        print("Tushlik vaqti!")
    elif vaqt >= 18.0 and vaqt <= 19.0:
        print("Kechki ovqat vaqti!")
    else:
        print("Ishlaymiz!")


def soatga_aylantir(vaqt):
    soat, daqiqa = vaqt.split(":")

    return float(soat) + float(daqiqa) / 60


main()
