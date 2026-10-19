import string

ism = input("Ismingiz nima? ").strip()
ism = string.capwords(ism)
print(f"Salom, {ism}")
