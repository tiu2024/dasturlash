matn = input("Matn: ")

natija = ""
for h in matn:
    if h.lower() not in "aeiou":
        natija += h

print(f"Natija: {natija}")
