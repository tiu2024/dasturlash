urinish = 0

while True:
    kod = input("PIN: ")
    urinish += 1
    if kod == "1234":
        print("Ochildi!")
        break
    if urinish == 3:
        print("Telefon bloklandi")
        break
