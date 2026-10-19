# Amaliyot

Bu sahifada [ma'ruzada](lecture.md) o'rganilgan `while` va `for` looplari hamda satrlar bilan 11 ta masala keltirilgan. Birinchi 7 tasi loop mashqlari, oxirgi 4 tasi Harvard universitetining CS50 Python kursi masalalariga asoslangan (har birida asl masalaga havola bor). Har bir masala shartidan keyin **Yechim** bloki joylashgan: u yopiq turadi, ustiga bosib oching. Avval masalani o'zingiz yechib ko'ring va natijani namuna bilan solishtiring, keyin yechim va tushuntirishni o'qing.

Har bir yechim ichida shu dasturning `.py` fayliga havola bor.

CS50 materiallari [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) litsenziyasi bilan tarqatiladi. Bu sahifadagi shartlar va yechimlar o'zbek tilida qayta yozilgan.

## 1. Sonlarni chiqarish

**Masala.** Shunday dastur yozing: butun `n` sonini so'raydi va 1 dan `n` gacha (`n` ham kiradi) sonlarni har birini yangi qatorda chiqaradi.

Namuna:

```text
n ni kiriting: 5
1
2
3
4
5
```

??? success "Yechim"

    ```python
    n = int(input("n ni kiriting: "))

    for i in range(1, n + 1):
        print(i)
    ```

    Fayl: [p1.py](../../../downloads/dasturlash/week-04/p1.py)

    **Tushuntirish.**

    - `range(1, n + 1)` — `1, 2, ..., n` sonlari. `range` da oxirgi son kirmaydi, shuning uchun `n` ham chiqishi uchun `n + 1` yozilgan ([ma'ruzada](lecture.md#range)).
    - Har aylanishda `i` navbatdagi songa teng bo'ladi va `print(i)` uni chiqaradi.
    - `range(1, n)` yozilsa, oxirgi son (`n`) chiqmaydi. Bu **off-by-one** xatosi.

## 2. 1 dan n gacha yig'indi

**Masala.** Butun `n` sonini so'rang va 1 dan `n` gacha (`n` ham kiradi) barcha sonlarning yig'indisini chiqaring.

Namuna:

```text
n ni kiriting: 100
1 dan 100 gacha yig'indi: 5050
```

```text
n ni kiriting: 10
1 dan 10 gacha yig'indi: 55
```

??? success "Yechim"

    ```python
    n = int(input("n ni kiriting: "))

    yigindi = 0
    for i in range(1, n + 1):
        yigindi += i

    print(f"1 dan {n} gacha yig'indi: {yigindi}")
    ```

    Fayl: [p2.py](../../../downloads/dasturlash/week-04/p2.py)

    **Tushuntirish.**

    - `yigindi = 0` — boshlang'ich qiymat. U loopdan oldin, bir marta yoziladi.
    - `yigindi += i` — `yigindi = yigindi + i` ning qisqa yozilishi: har aylanishda `i` yig'indiga qo'shiladi.
    - `n = 100` uchun natija `5050` — ma'ruzadagi [Gauss misoli](lecture.md#savol-gauss-xato-qildimi) bilan bir xil. Loop `range(1, n + 1)` bilan yozilgani uchun `100` ham qo'shiladi.
    - `n = 1` bo'lsa, natija `1`.

## 3. Karra jadvali

**Masala.** Butun sonni so'rang va uning 1 dan 10 gacha karra jadvalini chiqaring.

Namuna:

```text
Son: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

??? success "Yechim"

    ```python
    son = int(input("Son: "))

    for i in range(1, 11):
        print(f"{son} x {i} = {son * i}")
    ```

    Fayl: [p3.py](../../../downloads/dasturlash/week-04/p3.py)

    **Tushuntirish.**

    - `range(1, 11)` — 1 dan 10 gacha, chunki 11 kirmaydi. Loop roppa-rosa 10 marta aylanadi.
    - `f"{son} x {i} = {son * i}"` — [f-string](../week-02/lecture.md#qiymatlarni-birga-chiqarish): `{ }` ichiga ifoda ham yozish mumkin, shuning uchun ko'paytma `{son * i}` da hisoblanadi.

## 4. Teskari sanoq

**Masala.** Butun `n` sonini so'rang. `n` dan 1 gacha teskari sanang (har bir son yangi qatorda), oxirida "Start!" deb chiqaring. `n = 0` bo'lsa, faqat "Start!" chiqsin.

Namuna:

```text
Qaysi sondan boshlaymiz? 3
3
2
1
Start!
```

```text
Qaysi sondan boshlaymiz? 0
Start!
```

??? success "Yechim"

    ```python
    n = int(input("Qaysi sondan boshlaymiz? "))

    for i in range(n, 0, -1):
        print(i)
    print("Start!")
    ```

    Fayl: [p4.py](../../../downloads/dasturlash/week-04/p4.py)

    **Tushuntirish.**

    - `range(n, 0, -1)` — `n` dan boshlab 1 gacha, qadam `-1`. `0` kirmaydi, chunki `stop` hech qachon kirmaydi.
    - `print("Start!")` chekinishsiz yozilgan, ya'ni loopdan **keyin**, bir marta bajariladi.
    - `n = 0` bo'lsa, `range(0, 0, -1)` bo'sh: loop bir marta ham aylanmaydi, xato ham chiqmaydi. Qadam yozilmasa (`range(3, 0)`) ham ketma-ketlik bo'sh bo'ladi ([ma'ruzadagi raketa misoli](lecture.md#savol-raketa-uchadimi)).

## 5. 0 kiritilguncha yig'indi

**Masala.** Foydalanuvchidan sonlarni birin-ketin so'rang. `0` kiritilganda so'rashni to'xtating va kiritilgan barcha sonlarning yig'indisini chiqaring (`0` o'zi hisobga kirmaydi).

Namuna:

```text
Son (to'xtatish uchun 0): 5
Son (to'xtatish uchun 0): 12
Son (to'xtatish uchun 0): -2
Son (to'xtatish uchun 0): 0
Yig'indi: 15
```

```text
Son (to'xtatish uchun 0): 0
Yig'indi: 0
```

??? success "Yechim"

    ```python
    jami = 0

    while True:
        son = int(input("Son (to'xtatish uchun 0): "))
        if son == 0:
            break
        jami += son

    print(f"Yig'indi: {jami}")
    ```

    Fayl: [p5.py](../../../downloads/dasturlash/week-04/p5.py)

    **Tushuntirish.**

    - Necha son kiritilishi oldindan noma'lum, shuning uchun `while True` ishlatilgan; loopdan `0` kiritilganda `break` bilan chiqiladi ([ma'ruzada](lecture.md#while-true-va-break)).
    - `jami = 0` loopdan oldin yoziladi, `jami += son` har aylanishda yangi sonni qo'shadi.
    - `if son == 0: break` tekshiruvi `jami += son` dan **oldin** turibdi, shuning uchun to'xtatuvchi `0` yig'indiga qo'shilmaydi.
    - Birinchi son `0` bo'lsa, loop darhol tugaydi va natija `0` bo'ladi.

## 6. PIN kod: 3 ta urinish

**Masala.** Telefon PIN kodini so'rang. To'g'ri PIN `1234`. To'g'ri kiritilsa, "Ochildi!" deb chiqaring va to'xtating. 3 ta urinishdan keyin ham to'g'ri kiritilmasa, "Telefon bloklandi" deb chiqaring va to'xtating.

Namuna:

```text
PIN: 0000
PIN: 1234
Ochildi!
```

```text
PIN: 1111
PIN: 2222
PIN: 3333
Telefon bloklandi
```

```text
PIN: 1111
PIN: 2222
PIN: 1234
Ochildi!
```

??? success "Yechim"

    ```python
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
    ```

    Fayl: [p6.py](../../../downloads/dasturlash/week-04/p6.py)

    **Tushuntirish.**

    - `urinish` — **sanagich**: loopdan oldin `0` ga tenglanadi, har so'rovdan keyin `1` ga oshadi.
    - Ikkita `break` bor: biri to'g'ri PIN uchun, ikkinchisi urinishlar tugaganda.
    - **Shartlar tartibi muhim.** To'g'ri PIN tekshiruvi birinchi turibdi, shuning uchun 3-urinishda kiritilgan to'g'ri `1234` ham "Ochildi!" natijasini beradi (oxirgi namunaga qarang). Ikki `if` o'rni almashtirilsa, 3-urinishda to'g'ri PIN kiritilsa ham telefon bloklanadi.
    - Bu dastur darsda jonli yozilgan.

## 7. Palindrom

**Masala.** So'z kiriting. Agar so'z chapdan o'ngga ham, o'ngdan chapga ham bir xil o'qilsa (palindrom), "Palindrom", aks holda "Palindrom emas" deb chiqaring. Katta va kichik harf farqlanmasin.

Namuna:

```text
So'z: kiyik
Palindrom
```

```text
So'z: kitob
Palindrom emas
```

```text
So'z: Anna
Palindrom
```

??? success "Yechim"

    ```python
    soz = input("So'z: ").lower()

    teskari = ""
    for h in soz:
        teskari = h + teskari

    if teskari == soz:
        print("Palindrom")
    else:
        print("Palindrom emas")
    ```

    Fayl: [p7.py](../../../downloads/dasturlash/week-04/p7.py)

    **Tushuntirish.**

    - `.lower()` ([2-haftada](../week-02/lecture.md#satrlar-bilan-ishlash)) so'zni kichik harflarga o'tkazadi. Busiz `"Anna"` ning teskarisi `"annA"` bo'lib, `"Anna"` ga teng bo'lmasdi.
    - Teskari so'z [ma'ruzadagidek](lecture.md#satr-ustida-loop) yasaladi: har bir yangi harf `teskari` ning **oldiga** yopishtiriladi (`h + teskari`).
    - `teskari == soz` — ikki satr teng bo'lsa `True`.
    - Bir harfli so'z (`"a"`) va bo'sh satr palindrom hisoblanadi.

## 8. Cola avtomati

**Masala.** Cola narxi 50 tiyin. Avtomat faqat 25, 10 va 5 tiyinlik tangalarni qabul qiladi. Dastur to'lanishi kerak bo'lgan summani chiqaradi va tanga so'raydi. Boshqa qiymatdagi tangalar e'tiborga olinmaydi (summa o'zgarmaydi). Summa to'liq to'langanda yoki oshib ketganda, qaytimni chiqaring.

Bu masala CS50 Python kursining [Coke Machine](https://cs50.harvard.edu/python/psets/2/coke/) masalasiga asoslangan.

Namuna:

```text
To'lanishi kerak: 50
Tanga soling: 25
To'lanishi kerak: 25
Tanga soling: 25
Qaytim: 0
```

```text
To'lanishi kerak: 50
Tanga soling: 25
To'lanishi kerak: 25
Tanga soling: 7
To'lanishi kerak: 25
Tanga soling: 10
To'lanishi kerak: 15
Tanga soling: 10
To'lanishi kerak: 5
Tanga soling: 10
Qaytim: 5
```

??? success "Yechim"

    ```python
    summa = 50

    while summa > 0:
        print(f"To'lanishi kerak: {summa}")
        tanga = int(input("Tanga soling: "))
        if tanga == 25 or tanga == 10 or tanga == 5:
            summa -= tanga

    print(f"Qaytim: {-summa}")
    ```

    Fayl: [p8.py](../../../downloads/dasturlash/week-04/p8.py)

    **Tushuntirish.**

    - Necha tanga kerak bo'lishi noma'lum, shuning uchun `while` ishlatilgan. Uning sharti `summa > 0`: pul yetmaguncha takrorlanadi ([ma'ruzada](lecture.md#while-yoki-for) `while pul < narx` kabi).
    - `tanga == 25 or tanga == 10 or tanga == 5` — [3-haftadagi](../week-03/lecture.md#or-yoki) `or`. `tanga == 25 or 10 or 5` deb yozish xato: u har doim `True` bo'ladi.
    - `7` kiritilganda `if` sharti `False`, `summa -= tanga` bajarilmaydi va summa o'zgarmaydi (ikkinchi namuna).
    - `summa -= tanga` — `summa = summa - tanga` ning qisqa yozilishi.
    - Loop tugaganda `summa` nolga teng yoki manfiy bo'ladi. Qaytim — uning ishorasi o'zgargani: `-summa`. Ikkinchi namunada `summa = -5`, qaytim `5`.

## 9. camelCase dan snake_case ga

**Masala.** Dasturchilar o'zgaruvchi nomlarini ikki usulda yozadi: `camelCase` (so'zlar birga, har bir keyingi so'z katta harf bilan: `firstName`) va `snake_case` (so'zlar kichik harf bilan, `_` bilan ajratilgan: `first_name`). `camelCase` nomni so'rang va uni `snake_case` ga o'tkazib chiqaring. Nom faqat lotin harflaridan iborat.

Bu masala CS50 Python kursining [camelCase](https://cs50.harvard.edu/python/psets/2/camel/) masalasiga asoslangan.

Namuna:

```text
camelCase nomi: firstName
snake_case nomi: first_name
```

```text
camelCase nomi: preferredFirstName
snake_case nomi: preferred_first_name
```

```text
camelCase nomi: ism
snake_case nomi: ism
```

??? success "Yechim"

    ```python
    camel = input("camelCase nomi: ")

    snake = ""
    for h in camel:
        if h.isupper():
            snake += "_" + h.lower()
        else:
            snake += h

    print(f"snake_case nomi: {snake}")
    ```

    Fayl: [p9.py](../../../downloads/dasturlash/week-04/p9.py)

    **Tushuntirish.**

    - Yangi: `h.isupper()` — `h` katta harf bo'lsa `True`, aks holda `False`. Masalan, `"F".isupper()` — `True`, `"f".isupper()` — `False`.
    - Har bir katta harf uchun `"_" + h.lower()` qo'shiladi: `N` → `_n`. Boshqa harflar o'zgarishsiz qo'shiladi.
    - `snake += ...` — satr oxiriga qo'shish. `snake` bo'sh satrdan (`""`) boshlanadi, ma'ruzadagi teskari so'z yasash kabi ([ma'ruzada](lecture.md#satr-ustida-loop)).
    - Katta harfsiz nom (`ism`) o'zgarmaydi.

## 10. Twttr: unlilarni olib tashlash

**Masala.** Ba'zi ijtimoiy tarmoqlar matndan unli harflarni olib tashlab, joy tejaydi (Twitter → Twttr). Matn so'rang va undan `a`, `e`, `i`, `o`, `u` harflarini (katta va kichik) olib tashlab chiqaring. Boshqa belgilar (undosh harflar, tinish belgilari, bo'sh joy) o'z joyida qoladi.

Bu masala CS50 Python kursining [Just setting up my twttr](https://cs50.harvard.edu/python/psets/2/twttr/) masalasiga asoslangan.

Namuna:

```text
Matn: Twitter
Natija: Twttr
```

```text
Matn: What's your name?
Natija: Wht's yr nm?
```

```text
Matn: Samarqand
Natija: Smrqnd
```

??? success "Yechim"

    ```python
    matn = input("Matn: ")

    natija = ""
    for h in matn:
        if h.lower() not in "aeiou":
            natija += h

    print(f"Natija: {natija}")
    ```

    Fayl: [p10.py](../../../downloads/dasturlash/week-04/p10.py)

    **Tushuntirish.**

    - `h.lower() not in "aeiou"` — `h` kichik harfga aylantirilib, `"aeiou"` satrida **yo'q**ligi tekshiriladi. `.lower()` tufayli `A` ham unli hisoblanadi, lekin `natija` ga `h` ning o'zi (asl harf) qo'shiladi.
    - Yangi: `not in` — `in` ning teskarisi ([ma'ruzada](lecture.md#in-va-find) `in` bor). `"x" not in "aeiou"` — `True`.
    - Natija bo'sh satrdan boshlab yig'iladi: unli bo'lmagan har bir belgi qo'shiladi.
    - Dastur faqat `a, e, i, o, u` ni olib tashlaydi. O'zbekcha `o'` dagi `o` ham unli sifatida o'chadi, `'` qoladi.

## 11. Avtoraqam tekshiruvi

**Masala.** Avtomobil raqami to'g'ri bo'lishi uchun quyidagi qoidalarning hammasi bajarilishi kerak:

- uzunligi 2 dan 6 gacha (ikkalasi ham kiradi);
- birinchi ikki belgi harf;
- raqamlar (agar bo'lsa) faqat oxirida turadi, ya'ni raqamdan keyin harf kelmaydi: `AB12C` noto'g'ri;
- birinchi raqam `0` bo'lmasligi kerak: `CS05` noto'g'ri;
- nuqta, bo'sh joy va boshqa tinish belgilari yo'q.

Raqamni so'rang va "To'g'ri raqam" yoki "Noto'g'ri raqam" deb chiqaring. Tekshiruvni `is_valid(s)` funksiyasiga yozing: u `True` yoki `False` qaytarsin.

Bu masala CS50 Python kursining [Vanity Plates](https://cs50.harvard.edu/python/psets/2/plates/) masalasiga asoslangan.

Namuna:

```text
Avtoraqam: CS50
To'g'ri raqam
```

```text
Avtoraqam: CS05
Noto'g'ri raqam
```

```text
Avtoraqam: PI3.14
Noto'g'ri raqam
```

```text
Avtoraqam: H
Noto'g'ri raqam
```

```text
Avtoraqam: OUTATIME
Noto'g'ri raqam
```

```text
Avtoraqam: AB12C
Noto'g'ri raqam
```

??? success "Yechim"

    ```python
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
    ```

    Fayl: [p11.py](../../../downloads/dasturlash/week-04/p11.py)

    **Tushuntirish.**

    - Dastur [3-haftadagi](../week-03/lecture.md#main-funksiyasi) `main()` shaklida yozilgan, tekshiruv esa `True` yoki `False` qaytaradigan alohida funksiyada ([mantiqiy funksiya](../week-03/lecture.md#mantiqiy-funksiyalar)).
    - Yangi: `s.isalpha()` — satrdagi barcha belgi harf bo'lsa `True`; `s.isdigit()` — barchasi raqam bo'lsa `True`. Bo'sh satr uchun ikkalasi ham `False`.
    - `len(s) < 2 or len(s) > 6` — uzunlik 2 dan kichik yoki 6 dan katta bo'lsa, raqam rad etiladi. Shuning uchun `H` va `OUTATIME` noto'g'ri.
    - `s[:2].isalpha()` — birinchi ikki belgi ([slice](lecture.md#slice-satrdan-bolak-olish)) harfmi.
    - `while` loop `i` ni birinchi harf bo'lmagan belgigacha suradi. `i < len(s)` sharti `s[i]` dan **oldin** turishi shart, aks holda oxiriga yetganda `IndexError` chiqadi.
    - `s[i:]` — harflardan keyingi qism. U bo'sh bo'lsa (`AB`), raqam to'g'ri. Bo'lmasa, u faqat raqamlardan iborat va `0` bilan boshlanmasligi kerak: `raqamlar.isdigit() and raqamlar[0] != "0"`.
    - Shuning uchun `AB12C` (`C` raqam emas), `PI3.14` (`.` raqam emas) va `CS05` (`0` bilan boshlanadi) rad etiladi.
    - `ab` kichik harflar bilan ham to'g'ri hisoblanadi: qoidalar katta-kichik harfni farqlamaydi.

## Qisqa lug'at

| Atama | Ma'nosi |
|---|---|
| `yigindi += i` | `yigindi = yigindi + i` ning qisqa yozilishi |
| `summa -= tanga` | `summa = summa - tanga` ning qisqa yozilishi |
| sanagich | loop ichida `+= 1` bilan oshib boradigan o'zgaruvchi (`urinish`) |
| `h.isupper()` | `h` katta harf bo'lsa `True` |
| `s.isalpha()` | `s` dagi barcha belgi harf bo'lsa `True` |
| `s.isdigit()` | `s` dagi barcha belgi raqam bo'lsa `True` |
| `a not in s` | `a` `s` ichida **yo'q** bo'lsa `True` |
| `snake += ...` | satr oxiriga qo'shish |
