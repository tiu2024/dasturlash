berish = 12010
olish = 11500

print("Dollar olish uchun 1ni bos.\nDollar berish uchun 2ni bos.")

tanlov = input("Tanlov? ")

if tanlov == "1":
    qiymat = int(input("Qancha som bor? "))
    natija = round(qiymat / berish)

    print(f"Shuncha boladi: {natija}. Kurs = {berish}")

elif tanlov == "2":
    qiymat = int(input("Qancha dollar kerak? "))
    natija = qiymat * berish

    print(f"Shuncha boladi: {natija}. Kurs = {olish}")

else:
    print("Bunday tanlov yoq.")