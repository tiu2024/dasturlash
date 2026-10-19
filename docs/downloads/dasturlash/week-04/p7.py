soz = input("So'z: ").lower()

teskari = ""
for h in soz:
    teskari = h + teskari

if teskari == soz:
    print("Palindrom")
else:
    print("Palindrom emas")
