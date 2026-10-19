sotish_kursi = 12010   # bank dollarni shu kursda sotadi
olish_kursi = 11500    # bank dollarni shu kursda sotib oladi

print("Dollar sotib olish uchun 1 ni bosing.\nDollar sotish uchun 2 ni bosing.")

tanlov = input("Tanlov? ")

if tanlov == "1":
    som = int(input("Qancha so'mingiz bor? "))
    dollar = som // sotish_kursi
    print(f"Siz {dollar} dollar olasiz. Kurs: {sotish_kursi}")
elif tanlov == "2":
    dollar = int(input("Necha dollar sotasiz? "))
    som = dollar * olish_kursi
    print(f"Siz {som} so'm olasiz. Kurs: {olish_kursi}")
else:
    print("Bunday tanlov yo'q.")
