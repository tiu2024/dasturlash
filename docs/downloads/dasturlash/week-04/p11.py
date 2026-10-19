def main():
    raqam = input("Avtoraqam: ")
    if is_valid(raqam):
        print("To'g'ri raqam")
    else:
        print("Noto'g'ri raqam")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False

    i = 0
    while i < len(s) and s[i].isalpha():
        i += 1

    raqamlar = s[i:]
    if raqamlar == "":
        return True
    return raqamlar.isdigit() and raqamlar[0] != "0"


main()
