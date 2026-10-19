summa = 50

while summa > 0:
    print(f"To'lanishi kerak: {summa}")
    tanga = int(input("Tanga soling: "))
    if tanga == 25 or tanga == 10 or tanga == 5:
        summa -= tanga

print(f"Qaytim: {-summa}")
