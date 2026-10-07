# Amaliyot

Bu sahifada [ma'ruzada](lecture.md) o'rganilgan funksiyalar va shartlar bilan darsda yechilgan 16 ta masala keltirilgan. Har bir masala shartidan keyin **Yechim** bloki joylashgan: u yopiq turadi, ustiga bosib oching. Avval masalani o'zingiz yechib ko'ring va natijani namuna bilan solishtiring, keyin yechim va tushuntirishni o'qing.

Har bir yechim ichida shu dasturning `.py` fayliga havola bor.

## 1. Ovoz berish huquqi

**Masala.** Shunday dastur yozing: yoshni so'raydi va 18 yoki undan katta bo'lsa "Ovoz bera olasiz", aks holda "Hali ovoz bera olmaysiz" deb javob beradi.

Namuna:

```text
Yoshingiz: 20
Ovoz bera olasiz
```

```text
Yoshingiz: 17
Hali ovoz bera olmaysiz
```

??? success "Yechim"

    ```python
    yosh = int(input("Yoshingiz: "))

    if yosh >= 18:
        print("Ovoz bera olasiz")
    else:
        print("Hali ovoz bera olmaysiz")
    ```

    Fayl: [p8.py](../../../downloads/dasturlash/week-03/p8.py)

    **Tushuntirish.**

    - `if shart:` — **shartli operator**. `shart` to'g'ri (`True`) bo'lsa, ostidagi (chekinish bilan yozilgan) qatorlar bajariladi. Shart oxiridagi `:` va keyingi qatorlardagi chekinish (4 ta probel) majburiy.
    - `yosh >= 18` — **taqqoslash** ifodasi. Natijasi `True` yoki `False` bo'ladi. Python'dagi taqqoslash operatorlari:

        | Operator | Ma'nosi | Misol |
        |:---:|---|---|
        | `==` | teng | `yosh == 18` |
        | `!=` | teng emas | `yosh != 18` |
        | `>` | katta | `yosh > 18` |
        | `<` | kichik | `yosh < 18` |
        | `>=` | katta yoki teng | `yosh >= 18` |
        | `<=` | kichik yoki teng | `yosh <= 18` |

    - `else:` — shart **to'g'ri bo'lmaganda** bajariladigan qism. Ikki blokdan **faqat bittasi** ishlaydi.
    - `=` va `==` ni adashtirmang: `=` qiymat **beradi** (`yosh = 18`), `==` esa qiymatlarni **solishtiradi** (`yosh == 18`).
    - **Chegaraviy qiymat.** `>=` tufayli aynan `18` yoshli odam ovoz bera oladi. `>` yozilsa, 18 yoshli ham "Hali ovoz bera olmaysiz" javobini olardi. Shartlarni har doim chegara qiymatlarida (`17`, `18`) tekshiring.
    - `int(input(...))` — yosh son sifatida solishtirilishi uchun matn butun songa aylantirilgan.

## 2. Son musbatmi?

**Masala.** Shunday dastur yozing: sonni so'raydi va u noldan katta bo'lsa "Musbat", aks holda "Manfiy" deb javob beradi.

Namuna:

```text
Son kiriting: 5
Musbat
```

```text
Son kiriting: -3
Manfiy
```

```text
Son kiriting: 0
Manfiy
```

??? success "Yechim"

    ```python
    son = int(input("Son kiriting: "))

    if son > 0:
        print("Musbat")
    else:
        print("Manfiy")
    ```

    Fayl: [p9.py](../../../downloads/dasturlash/week-03/p9.py)

    **Tushuntirish.**

    - Dastur `5` va `-3` uchun to'g'ri ishlaydi, lekin `0` uchun **noto'g'ri**: nol musbat ham, manfiy ham emas, ammo `son > 0` shartiga tushmagani uchun `else` ishlaydi va "Manfiy" chiqadi.
    - Bu **mantiqiy xato** (*logic error*): dastur xatosiz ishlaydi, lekin noto'g'ri natija beradi. Bunday xatolarni faqat turli qiymatlar, ayniqsa **chegaraviy qiymatlar** (`0`, `1`, `-1`) bilan sinash orqali topish mumkin.
    - Keyingi masalada xato `elif` yordamida tuzatiladi.

## 3. Musbat, manfiy yoki nol

**Masala.** Shunday dastur yozing: oldingi masalani to'g'rilang: nol uchun "Nol" javobi ham chiqsin.

Namuna:

```text
Son kiriting: 8
Musbat
```

```text
Son kiriting: -8
Manfiy
```

```text
Son kiriting: 0
Nol
```

??? success "Yechim"

    ```python
    son = int(input("Son kiriting: "))

    if son > 0:
        print("Musbat")
    elif son < 0:
        print("Manfiy")
    else:
        print("Nol")
    ```

    Fayl: [p10.py](../../../downloads/dasturlash/week-03/p10.py)

    **Tushuntirish.**

    - `elif` ("else if") — oldingi shart bajarilmaganda **yana bir shartni** tekshiradi. Shartlar **yuqoridan pastga** tekshiriladi va **birinchi to'g'ri chiqqan** blokgina bajariladi; qolganlari o'tkazib yuboriladi.
    - Oxirgi `else` — yuqoridagi hech bir shart to'g'ri bo'lmaganda ishlaydi. Bu yerda `son > 0` ham, `son < 0` ham yolg'on bo'lsa, demak son `0` ga teng.
    - Struktura: bitta `if`, istalgancha `elif` va ixtiyoriy bitta `else`.
    - 2-masalada nol noto'g'ri javob olgan edi; endi `0` uchun `Nol` chiqadi.

## 4. Teatr chiptasi

**Masala.** Shunday dastur yozing: yoshga qarab chipta narxini chiqaradi: 12 yoshgacha — 20 000, 12 dan 60 gacha — 40 000, 60 va undan kattalar — 25 000 so'm.

Namuna:

```text
Yoshingiz: 8
Chipta narxi: 20 000 so'm
```

```text
Yoshingiz: 30
Chipta narxi: 40 000 so'm
```

```text
Yoshingiz: 65
Chipta narxi: 25 000 so'm
```

??? success "Yechim"

    ```python
    yosh = int(input("Yoshingiz: "))

    if yosh < 12:
        print("Chipta narxi: 20 000 so'm")
    elif yosh < 60:
        print("Chipta narxi: 40 000 so'm")
    else:
        print("Chipta narxi: 25 000 so'm")
    ```

    Fayl: [p13.py](../../../downloads/dasturlash/week-03/p13.py)

    **Tushuntirish.**

    - Shartlar yuqoridan pastga tekshiriladi, shuning uchun `elif yosh < 60` ga yetib kelgan odam allaqachon `yosh < 12` shartidan o'tmagan, ya'ni `yosh >= 12`. Shu sababli `yosh >= 12 and yosh < 60` deb yozish shart emas.
    - Oraliqlar chegaralari: `11` → 20 000; `12` → 40 000; `59` → 40 000; `60` → 25 000. Chegaralar `<` bilan yozilgani uchun 12 yoshli bolalar toifasiga kirmaydi, 60 yoshli esa uchinchi toifaga kiradi.
    - Shartlar tartibi muhim: agar `yosh < 60` ni birinchi yozsak, 5 yoshli bola ham 40 000 to'laydi.

## 5. Yetkazib berish narxi

**Masala.** Shunday dastur yozing: posilka og'irligiga qarab yetkazib berish narxini chiqaradi: 1 kg gacha — 15 000, 5 kg gacha — 30 000, undan og'ir bo'lsa — 50 000 so'm.

Namuna:

```text
Og'irligi (kg): 1
Yetkazib berish: 15 000 so'm
```

```text
Og'irligi (kg): 3
Yetkazib berish: 30 000 so'm
```

```text
Og'irligi (kg): 10
Yetkazib berish: 50 000 so'm
```

??? success "Yechim"

    ```python
    vazn = int(input("Og'irligi (kg): "))

    if vazn <= 1:
        print("Yetkazib berish: 15 000 so'm")
    elif vazn <= 5:
        print("Yetkazib berish: 30 000 so'm")
    else:
        print("Yetkazib berish: 50 000 so'm")
    ```

    Fayl: [p14.py](../../../downloads/dasturlash/week-03/p14.py)

    **Tushuntirish.**

    - Bu 4-masaladagi usulning o'zi: shartlar o'sish tartibida yoziladi, har bir keyingi `elif` oldingisining "davomi" bo'ladi.
    - `<=` (kichik yoki teng) chegarani **kiritadi**: aynan `1` kg → 15 000, `5` kg → 30 000, `6` kg → 50 000.
    - `vazn` `int` sifatida o'qilgani uchun `0.5` kabi kasr qiymat kiritilsa, `ValueError` chiqadi. Kasr vaznlar kerak bo'lsa, `float(input(...))` ishlatiladi.

## 6. Oy nomi

**Masala.** Shunday dastur yozing: oy raqamini (1–12) so'raydi va oy nomini chiqaradi. Boshqa raqam uchun "Bunday oy yo'q" deb javob beradi.

Namuna:

```text
Oy raqami: 3
Mart
```

```text
Oy raqami: 12
Dekabr
```

```text
Oy raqami: 13
Bunday oy yo'q
```

??? success "Yechim"

    ```python
    oy = int(input("Oy raqami: "))

    if oy == 1:
        print("Yanvar")
    elif oy == 2:
        print("Fevral")
    elif oy == 3:
        print("Mart")
    elif oy == 4:
        print("Aprel")
    elif oy == 5:
        print("May")
    elif oy == 6:
        print("Iyun")
    elif oy == 7:
        print("Iyul")
    elif oy == 8:
        print("Avgust")
    elif oy == 9:
        print("Sentyabr")
    elif oy == 10:
        print("Oktyabr")
    elif oy == 11:
        print("Noyabr")
    elif oy == 12:
        print("Dekabr")
    else:
        print("Bunday oy yo'q")
    ```

    Fayl: [p11.py](../../../downloads/dasturlash/week-03/p11.py)

    **Tushuntirish.**

    - Ko'p `elif` ketma-ketligi: har bir raqam alohida tekshiriladi, tegishli blok topilganda qolganlari tekshirilmaydi.
    - `oy == 3` — son bilan taqqoslash; `oy` `int()` bilan songa aylantirilgan. Agar `int()` bo'lmasa, `"3" == 3` **yolg'on** bo'lar edi, chunki matn va son — har xil turlar.
    - Oxirgi `else` — "himoya" vazifasini bajaradi: `0`, `13`, `-5` kabi noto'g'ri qiymatlarni ushlaydi. Foydalanuvchi kiritishi mumkin bo'lgan **barcha** holatlarni o'ylab ko'rish yaxshi odat.
    - Bunday uzun zanjir ishlaydi, ammo takrorlanuvchi. Keyinchalik shunday masalalarni qisqaroq usullar bilan yechishni o'rganamiz.

## 7. Hafta kuni

**Masala.** Shunday dastur yozing: kun raqamini (1–7) so'raydi va hafta kuni nomini chiqaradi. Boshqa raqam uchun "Bunday kun yo'q" deb javob beradi.

Namuna:

```text
Kun raqami: 1
Dushanba
```

```text
Kun raqami: 7
Yakshanba
```

```text
Kun raqami: 8
Bunday kun yo'q
```

??? success "Yechim"

    ```python
    kun = int(input("Kun raqami: "))

    if kun == 1:
        print("Dushanba")
    elif kun == 2:
        print("Seshanba")
    elif kun == 3:
        print("Chorshanba")
    elif kun == 4:
        print("Payshanba")
    elif kun == 5:
        print("Juma")
    elif kun == 6:
        print("Shanba")
    elif kun == 7:
        print("Yakshanba")
    else:
        print("Bunday kun yo'q")
    ```

    Fayl: [p12.py](../../../downloads/dasturlash/week-03/p12.py)

    **Tushuntirish.**

    - Oldingi masala bilan bir xil g'oya: raqam bo'yicha `elif` zanjiri va noto'g'ri qiymatlar uchun `else`.
    - Chegaralarni sinang: `1` (Dushanba), `7` (Yakshanba), `0` va `8` (xato qiymatlar).

## 8. Uchta sondan eng kattasi

**Masala.** Shunday dastur yozing: uchta butun son oladi va ulardan eng kattasini chiqaradi.

Namuna:

```text
1-son: 3
2-son: 9
3-son: 5
Eng kattasi: 9
```

```text
1-son: 7
2-son: 7
3-son: 2
Eng kattasi: 7
```

??? success "Yechim"

    ```python
    a = int(input("1-son: "))
    b = int(input("2-son: "))
    c = int(input("3-son: "))

    if a >= b and a >= c:
        print("Eng kattasi:", a)
    elif b >= c:
        print("Eng kattasi:", b)
    else:
        print("Eng kattasi:", c)
    ```

    Fayl: [p15.py](../../../downloads/dasturlash/week-03/p15.py)

    **Tushuntirish.**

    - `and` — **mantiqiy "va"**: ikkala shart ham to'g'ri bo'lsa, natija `True`. `a >= b and a >= c` — "`a` `b` dan ham, `c` dan ham kichik emas".
    - Agar birinchi shart (`a` eng katta) bajarilmasa, `a` aniq eng katta emas. Qolgan ikki son orasidan kattasini tanlash uchun bitta taqqoslash — `b >= c` — yetarli: to'g'ri bo'lsa `b`, aks holda `c`.
    - `>=` ishlatilgani uchun teng sonlar ham to'g'ri ishlaydi: `7, 7, 2` → `7`; `4, 4, 4` → `4`.
    - Mantiqiy operatorlar: `and` ("va"), `or` ("yoki"), `not` ("emas").

## 9. Tosh, qaychi, qog'oz

**Masala.** Shunday dastur yozing: ikki o'yinchining tanlovini (`tosh`, `qaychi`, `qog'oz`) oladi va g'olibni aniqlaydi.

Namuna:

```text
1-o'yinchi: tosh
2-o'yinchi: qaychi
1-o'yinchi yutdi
```

```text
1-o'yinchi: qog'oz
2-o'yinchi: qaychi
2-o'yinchi yutdi
```

```text
1-o'yinchi: tosh
2-o'yinchi: tosh
Durang
```

??? success "Yechim"

    ```python
    o1 = input("1-o'yinchi: ")
    o2 = input("2-o'yinchi: ")

    if o1 == o2:
        print("Durang")
    elif o1 == "tosh" and o2 == "qaychi":
        print("1-o'yinchi yutdi")
    elif o1 == "qaychi" and o2 == "qog'oz":
        print("1-o'yinchi yutdi")
    elif o1 == "qog'oz" and o2 == "tosh":
        print("1-o'yinchi yutdi")
    else:
        print("2-o'yinchi yutdi")
    ```

    Fayl: [p16.py](../../../downloads/dasturlash/week-03/p16.py)

    **Tushuntirish.**

    - Matnlar ham `==` bilan solishtiriladi: `o1 == o2` ikkala o'yinchi bir xil narsa tanlaganini tekshiradi → durang.
    - Birinchi o'yinchi yutadigan uchta holat: tosh qaychini, qaychi qog'ozni, qog'oz toshni yengadi. Ularning har biri `and` bilan yoziladi: ikkala o'yinchining tanlovi **bir vaqtda** mos kelishi kerak.
    - `else` — qolgan holatlar: durang ham emas, birinchi o'yinchi ham yutmagan → ikkinchi o'yinchi yutdi.
    - Matn solishtirish **katta-kichik harfni va aniq belgilarni** hisobga oladi: `Tosh` yoki `tosh ` (oxirida probel bilan) kiritilsa, shart bajarilmaydi. `qog'oz` dagi apostrof ham aynan shunday yozilishi kerak. Kiritilgan matnni `.strip().lower()` bilan tozalash yaxshi usul.
    - Dastur noto'g'ri so'zlarni tekshirmaydi: masalan, `tosh` va `salom` kiritilsa, ham `else` ishlab, "2-o'yinchi yutdi" chiqadi.

## 10. Parol tekshiruvi

**Masala.** Shunday dastur yozing: parolni so'raydi. Parol `42`, `qirriq ikki` yoki `qirriq-ikki` bo'lsa (harf registridan qat'i nazar), "Togri parol", aks holda "Notogri parol" deb javob beradi.

Namuna:

```text
Parol? 42
Togri parol
```

```text
Parol? Qirriq Ikki
Togri parol
```

```text
Parol? 12345
Notogri parol
```

??? success "Yechim"

    ```python
    parol = input("Parol? ").lower()

    if parol == "42":
        print("Togri parol")
    elif parol == "qirriq ikki" or parol == "qirriq-ikki":
        print("Togri parol")
    else:
        print("Notogri parol")
    ```

    Fayl: [p3.py](../../../downloads/dasturlash/week-03/p3.py)

    **Tushuntirish.**

    - `.lower()` — kiritilgan matnni kichik harflarga o'tkazadi, shuning uchun `Qirriq Ikki`, `QIRRIQ IKKI` va `qirriq ikki` bir xil hisoblanadi.
    - `or` — **mantiqiy "yoki"**: ikki shartdan kamida bittasi to'g'ri bo'lsa, natija `True`. Parolning ikki yozilishidan istalgani qabul qilinadi.
    - `parol == "42"` — bu yerda `"42"` **matn**, chunki `input()` matn qaytaradi. `parol == 42` yolg'on bo'lardi.
    - Odatiy xato: `parol == "qirriq ikki" or "qirriq-ikki"` yozish. Bu **har doim to'g'ri** bo'ladi, chunki bo'sh bo'lmagan matn Python'da `True` hisoblanadi. Har bir taqqoslashni to'liq yozing: `parol == "a" or parol == "b"`.
    - Ikkala to'g'ri variantda ham bir xil xabar chiqadi; shartlarni `or` bilan birlashtirib, bitta `if` ga ham yozish mumkin edi.

## 11. Salomga mukofot

**Masala.** Shunday dastur yozing: "Yaxshimisan?" deb so'raydi. Javob "assalom" bilan boshlansa — "Mana senga $100", "salom" bilan boshlansa — "Mana senga $20", aks holda "Ha zor!" deb javob beradi.

Namuna:

```text
Yaxshimisan? Assalomu alaykum
Mana senga $100
```

```text
Yaxshimisan? Salom!
Mana senga $20
```

```text
Yaxshimisan? Yaxshi
Ha zor!
```

??? success "Yechim"

    ```python
    salom = input("Yaxshimisan? ").lower()

    if salom.startswith("assalom"):
        print("Mana senga $100")
    elif salom.startswith("salom"):
        print("Mana senga $20")
    else:
        print("Ha zor!")
    ```

    Fayl: [p4.py](../../../downloads/dasturlash/week-03/p4.py)

    **Tushuntirish.**

    - `satr.startswith(boshi)` — satr berilgan matn bilan **boshlansa** `True`, aks holda `False` qaytaradi. `"assalomu alaykum".startswith("assalom")` → `True`.
    - Shuning uchun `Assalomu alaykum`, `Assalom!` yoki `assalom` — barchasi mos keladi: butun so'zni emas, faqat boshlanishini tekshiramiz.
    - `.lower()` ni zanjirda oldindan chaqirib, `Salom` va `SALOM` ni ham ushlaymiz.
    - Teskarisini tekshiradigan metod ham bor: `satr.endswith(oxiri)`. Uni 15-masalada ko'ramiz.
    - `startswith` `True` / `False` qaytargani uchun u to'g'ridan-to'g'ri `if` / `elif` ichida ishlatiladi.

## 12. Oddiy kalkulyator

**Masala.** Shunday dastur yozing: "son amal son" ko'rinishidagi ifodani (masalan, `3 + 4`) oladi va natijani chiqaradi. Nolga bo'lishda va noma'lum amalda xabar beradi.

Namuna:

```text
Amal: 3 + 4
Natjia: 7.0
```

```text
Amal: 10 / 4
Natija: 2.5
```

```text
Amal: 5 / 0
O ga bolb bolmaydi!
```

```text
Amal: 5 ^ 2
Bunday amal yoq!
```

??? success "Yechim"

    ```python
    x, y, z = input("Amal: ").split()

    x = float(x)
    z = float(z)

    if y == '+':
        print("Natjia:", x + z)
    elif y == "-":
        print("Natija:", x - z)
    elif y == "*":
            print("Natija:", x * z)
    elif y == "/":
        if z == 0:
            print("O ga bolb bolmaydi!")
        else:
            print("Natija:", x / z)
    else:
        print("Bunday amal yoq!")
    ```

    Fayl: [p5.py](../../../downloads/dasturlash/week-03/p5.py)

    **Tushuntirish.**

    - `x, y, z = input("Amal: ").split()` — kiritilgan satr bo'sh joylar bo'yicha uch bo'lakka ajratiladi: `"3 + 4"` → `"3"`, `"+"`, `"4"`. Ular mos ravishda `x`, `y`, `z` ga saqlanadi. Shuning uchun foydalanuvchi sonlar va amalni **probellar bilan** yozishi shart: `3+4` (probelsiz) xato beradi (`ValueError`).
    - `x = float(x)`, `z = float(z)` — sonlar `float` ga aylantiriladi, shunda butun va kasr sonlar bilan ishlaydi. Amal belgisi `y` matn bo'lib qoladi.
    - Har bir `elif` amal belgisini matn sifatida tekshiradi: `y == "-"`.
    - **Ichma-ich shart.** `/` tarmog'ida yana bir `if` bor: avval `z == 0` tekshiriladi, shundagina bo'lish bajariladi. Nolga bo'lishning oldini olish uchun shu zarur.
    - Natija `float` bo'lgani uchun `3 + 4` → `7.0` chiqadi.
    - `else` — noma'lum amal (`^`, `%` va boshqalar) uchun.
    - `*` tarmog'idagi chekinish boshqalardan kattaroq: Python buni qabul qiladi, chunki blok ichida chekinish izchil. Lekin o'qishni osonlashtirish uchun doim bir xil, 4 probelli chekinishdan foydalaning.

## 13. Valyuta ayirboshlash

**Masala.** Shunday dastur yozing: foydalanuvchiga menyu ko'rsatadi (1 — dollar olish, 2 — dollar berish), tanlov bo'yicha so'ralgan miqdorni hisoblaydi.

Namuna:

```text
Dollar olish uchun 1ni bos.
Dollar berish uchun 2ni bos.
Tanlov? 1
Qancha som bor? 120100
Shuncha boladi: 10. Kurs = 12010
```

```text
Dollar olish uchun 1ni bos.
Dollar berish uchun 2ni bos.
Tanlov? 2
Qancha dollar kerak? 10
Shuncha boladi: 120100. Kurs = 11500
```

```text
Dollar olish uchun 1ni bos.
Dollar berish uchun 2ni bos.
Tanlov? 3
Bunday tanlov yoq.
```

??? success "Yechim"

    ```python
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
    ```

    Fayl: [p2.py](../../../downloads/dasturlash/week-03/p2.py)

    **Tushuntirish.**

    - `\n` — matn ichidagi **yangi qator** belgisi. Shuning uchun bitta `print()` ikki qatorni chiqaradi.
    - `tanlov = input("Tanlov? ")` — tanlov **matn** sifatida saqlanadi. Shuning uchun taqqoslash `tanlov == "1"` (tirnoq bilan); `tanlov == 1` hech qachon to'g'ri bo'lmaydi.
    - `if` / `elif` / `else` — menyuning ikki tanlovi va noto'g'ri tanlov uchun javob.
    - `round(qiymat / berish)` — bo'lish natijasi kasr bo'lishi mumkin, `round()` uni butun songa yaxlitlaydi.
    - Kurslar (`berish`, `olish`) dastur boshida o'zgaruvchilarga saqlangan. Kurs o'zgarsa, faqat shu ikki qatorni o'zgartirish kifoya.
    - `f"...{natija}. Kurs = {berish}"` — f-string bilan matn va qiymatlar birga chiqariladi.

## 14. Ovqat vaqti

**Masala.** Shunday dastur yozing: soatni `soat:daqiqa` ko'rinishida (masalan, `7:30`) oladi va nonushta (7:00–8:00), tushlik (12:00–13:00) yoki kechki ovqat (18:00–19:00) vaqti ekanini aytadi, aks holda "Ishlaymiz!" deydi.

Namuna:

```text
Soat nechida boldi? 7:30
Nonushta vaqti!
```

```text
Soat nechida boldi? 12:45
Tushlik vaqti!
```

```text
Soat nechida boldi? 9:15
Ishlaymiz!
```

??? success "Yechim"

    ```python
    def main():
        vaht = input("Soat nechida boldi? ")

        vaht = convert(vaht)

        if vaht >= 7.0 and vaht <= 8.0:
            print("Nonushta vaqti!")
        elif vaht >= 12.0 and vaht < 13.0:
            print("Tushlik vaqti!")
        elif vaht >= 18.0 and vaht < 19.0:
            print("Kechki ovqat vaqti!")
        else:
            print("Ishlaymiz!")

    def convert(vaht):
        soat, minut = vaht.split(":")

        return float(soat) + (float(minut) / 60)

    main()
    ```

    Fayl: [p6.py](../../../downloads/dasturlash/week-03/p6.py)

    **Tushuntirish.**

    - `vaht.split(":")` — satrni `:` belgisi bo'yicha bo'ladi: `"7:30".split(":")` → `["7", "30"]`. Argument sifatida ajratgich beriladi (argumentsiz `split()` bo'sh joy bo'yicha bo'ladi).
    - `soat, minut = ...` — ro'yxat elementlari ikki o'zgaruvchiga ochiladi.
    - `float(soat) + float(minut) / 60` — vaqtni **soat birligida** bitta songa aylantiradi: `7:30` → `7 + 30/60` = `7.5`. Shunday qilib vaqtni oddiy son sifatida solishtirish mumkin.
    - `return` — hisoblangan sonni `main()` ga qaytaradi. `vaht = convert(vaht)` da `vaht` matndan songa o'zgaradi.
    - `vaht >= 7.0 and vaht <= 8.0` — **oraliq** tekshiruvi: ikkala shart ham to'g'ri bo'lishi kerak. Python'da buni qisqa yozish ham mumkin: `7.0 <= vaht <= 8.0`.
    - Chegaralar: `7:00` va `8:00` nonushta vaqtiga kiradi (`<= 8.0`), tushlik va kechki ovqat esa soat oxirigacha (`< 13.0`, `< 19.0`) hisoblanadi: `12:59` → tushlik, `13:00` → "Ishlaymiz!".
    - Vaqt `soat:daqiqa` ko'rinishida kiritilishi shart; ikki nuqtasiz kiritilsa, `ValueError` chiqadi.

## 15. Ismni ajratib olish

**Masala.** Shunday dastur yozing: to'liq ismni (ism va familiya, istalgan tartibda) oladi va faqat ismga salom beradi. Familiya `ov` yoki `ova` bilan tugaydi deb hisoblang.

Namuna:

```text
F.I.O? karimov ali
Salom, Ali
```

```text
F.I.O? dilnoza yusupova
Salom, Dilnoza
```

??? success "Yechim"

    ```python
    def main():
        toliq_ism = input("F.I.O? ").title()

        print(f"Salom, {ism_ajratish(toliq_ism)}")

    def ism_ajratish(ism):
        name1, name2 = ism.split()

        if name1.endswith("ov") or name1.endswith("ova"):
            return name2

        return name1

    # def ism_ajratish(ism):
    #     name1, name2 = ism.split()

    #     if name1.endswith("ov") or name1.endswith("ova"):
    #         ism = name2
    #         familiya = name1
    #     else:
    #         ism = name1
    #         familiya = name2

    #     return ism

    def familiya_ajratish(ism):
        name1, name2 = ism.split()

        if name1.endswith("ov") or name1.endswith("ova"):
            ism = name2
            familiya = name1
        else:
            ism = name1
            familiya = name2

        return familiya

    main()
    ```

    Fayl: [p1.py](../../../downloads/dasturlash/week-03/p1.py)

    **Tushuntirish.**

    - `input(...).title()` — kiritilgan matnning har bir so'zi bosh harf bilan boshlanadi (`karimov ali` → `Karimov Ali`).
    - `name1, name2 = ism.split()` — to'liq ism ikki so'zga ajratiladi va ikki o'zgaruvchiga saqlanadi.
    - `satr.endswith(oxiri)` — satr berilgan matn bilan **tugasa** `True` qaytaradi. `"Karimov".endswith("ov")` → `True`. (`startswith` ning teskarisi.)
    - `name1.endswith("ov") or name1.endswith("ova")` — birinchi so'z familiyaga o'xshasa (`ov` yoki `ova` bilan tugasa), ism ikkinchi so'z (`name2`) bo'ladi.
    - **Erta `return`.** `return name2` bajarilishi bilan funksiya **darhol tugaydi**; keyingi qator (`return name1`) bajarilmaydi. Shart to'g'ri bo'lmasa, `if` bloki o'tkazib yuboriladi va `return name1` ishlaydi. Shuning uchun bu yerda `else` yozish shart bo'lmagan.
    - `print(f"Salom, {ism_ajratish(toliq_ism)}")` — f-string ichida funksiya chaqiruvi ham yozish mumkin: funksiya qaytargan qiymat shu joyga qo'yiladi.
    - Izohga olingan (`#`) kod — shu funksiyaning boshqa varianti; `familiya_ajratish()` esa familiyani qaytaradi. Hozir u chaqirilmayapti.
    - **Cheklovlar.** Dastur aynan ikki so'zni kutadi; boshqa son kiritilsa `ValueError` chiqadi. `ov`/`ova` bilan tugamaydigan familiyalar (masalan, `Aliyev`) bo'lsa, tartib noto'g'ri aniqlanadi: `Aliyev Vali` → `Salom, Aliyev`.

## 16. To'rtburchak yuzi

**Masala.** Shunday dastur yozing: to'rtburchakning uzunligi va enini oladi, yuzini hisoblab chiqaradigan funksiya yozing.

Namuna:

```text
Uzunlik: 5
Eni: 3
Yuzi: 15
```

??? success "Yechim"

    ```python
    def yuza(uzunlik, eni):
        print("Yuzi:", uzunlik * eni)

    a = int(input("Uzunlik: "))
    b = int(input("Eni: "))
    yuza(a, b)
    ```

    Fayl: [p7.py](../../../downloads/dasturlash/week-03/p7.py)

    **Tushuntirish.**

    - `def yuza(uzunlik, eni):` — ikki **parametrli** funksiya. `yuza(a, b)` chaqirilganda `a` qiymati `uzunlik` ga, `b` qiymati `eni` ga **tartib bo'yicha** o'tadi.
    - Funksiya e'lon qilinishi (`def`) uni **ishga tushirmaydi**; faqat `yuza(a, b)` qatori chaqirganda ishlaydi.
    - Funksiya ichida `return` yo'q: natija ekranga chiqariladi, lekin qaytarilmaydi. Shuning uchun `y = yuza(5, 3)` desak, `y` ichida `None` bo'ladi. Natijani keyinchalik ishlatmoqchi bo'lsak (masalan, `yuza(5, 3) * 2`), `print` o'rniga `return uzunlik * eni` yozish kerak.
    - Funksiya tanasidagi `uzunlik` va `eni` o'zgaruvchilari faqat funksiya ichida mavjud; `a` va `b` esa funksiyadan tashqarida.

## Qisqa lug'at

| Tushuncha | Ma'nosi |
|---|---|
| `if` / `elif` / `else` | shart bo'yicha tarmoqlanish; birinchi to'g'ri shartning bloki bajariladi |
| `==`, `!=`, `>`, `<`, `>=`, `<=` | taqqoslash operatorlari (natijasi `True` / `False`) |
| `and`, `or`, `not` | mantiqiy "va", "yoki", "emas" |
| `satr.startswith(x)` / `endswith(x)` | satr `x` bilan boshlansa / tugasa `True` |
| `satr.split(ajratgich)` | satrni ajratgich bo'yicha bo'laklarga bo'ladi |
