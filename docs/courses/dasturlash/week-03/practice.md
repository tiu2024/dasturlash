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

    Fayl: [p1.py](../../../downloads/dasturlash/week-03/p1.py)

    **Tushuntirish.**

    - `if shart:` — **shartli operator**. `shart` `True` bo'lsa, ostidagi (chekinish bilan yozilgan) qatorlar bajariladi. Shart oxiridagi `:` va keyingi qatorlardagi chekinish (4 ta probel) majburiy.
    - `yosh >= 18` — **taqqoslash** ifodasi. Natijasi `True` yoki `False` bo'ladi. Barcha taqqoslash operatorlari [ma'ruzada](lecture.md#taqqoslash-operatorlari) jadvalda berilgan.
    - `else:` — shart `False` bo'lganda bajariladigan qism. Ikki blokdan **faqat bittasi** ishlaydi.
    - **Chegaraviy qiymat.** `>=` tufayli aynan `18` yoshli odam ovoz bera oladi. `>` yozilsa, 18 yoshli ham "Hali ovoz bera olmaysiz" javobini olardi. Shartlarni har doim chegara qiymatlarida (`17`, `18`) tekshiring.
    - `int(input(...))` — yosh son sifatida solishtirilishi uchun matn butun songa aylantirilgan.

## 2. Son musbatmi?

**Masala.** Shunday dastur yozing: sonni so'raydi va u noldan katta bo'lsa "Musbat", aks holda "Manfiy" deb javob beradi.

!!! question "Diqqat"
    Bu masalaning sharti ataylab xato qo'yilgan. Oxirgi namunaga qarang: nol uchun javob to'g'rimi? Yechimni ochishdan oldin xatoni o'zingiz topishga harakat qiling.

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

    Fayl: [p2.py](../../../downloads/dasturlash/week-03/p2.py)

    **Tushuntirish.**

    - Dastur `5` va `-3` uchun to'g'ri ishlaydi, lekin `0` uchun **noto'g'ri**: nol musbat ham, manfiy ham emas, ammo `son > 0` sharti `False` bo'lgani uchun `else` ishlaydi va "Manfiy" chiqadi.
    - Bu **mantiqiy xato** (*logic error*): dastur xatosiz ishlaydi, lekin noto'g'ri natija beradi. Bunday xatolarni faqat turli qiymatlar, ayniqsa **chegaraviy qiymatlar** (`0`, `1`, `-1`) bilan sinash orqali topish mumkin.
    - Keyingi masalada xato `elif` yordamida tuzatiladi.

## 3. Musbat, manfiy yoki nol

**Masala.** Oldingi masaladagi dasturni to'g'rilang: nol uchun "Nol" javobi chiqsin.

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

    Fayl: [p3.py](../../../downloads/dasturlash/week-03/p3.py)

    **Tushuntirish.**

    - `elif` ("else if") — oldingi shart `False` bo'lganda **yana bir shartni** tekshiradi. Shartlar **yuqoridan pastga** tekshiriladi va sharti `True` bo'lgan **birinchi** blokgina bajariladi; qolganlari o'tkazib yuboriladi.
    - Oxirgi `else` — yuqoridagi hech bir shart `True` bo'lmaganda ishlaydi. Bu yerda `son > 0` ham, `son < 0` ham `False` bo'lsa, demak son `0` ga teng.
    - 2-masalada nol noto'g'ri javob olgan edi; endi `0` uchun `Nol` chiqadi.

## 4. Teatr chiptasi

**Masala.** Shunday dastur yozing: yoshga qarab chipta narxini chiqaradi:

- 0–11 yosh — 20 000 so'm;
- 12–59 yosh — 40 000 so'm;
- 60 yosh va undan katta — 25 000 so'm.

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

    Fayl: [p4.py](../../../downloads/dasturlash/week-03/p4.py)

    **Tushuntirish.**

    - Shartlar yuqoridan pastga tekshiriladi. Dastur `elif yosh < 60` gacha yetib kelgan bo'lsa, `yosh < 12` sharti `False` chiqqan, ya'ni `yosh >= 12`. Shu sababli `yosh >= 12 and yosh < 60` deb yozish shart emas.
    - Oraliqlar chegaralari: `11` → 20 000; `12` → 40 000; `59` → 40 000; `60` → 25 000. Chegaralar `<` bilan yozilgani uchun 12 yoshli bolalar toifasiga kirmaydi, 60 yoshli esa uchinchi toifaga kiradi.
    - Shartlar tartibi muhim: agar `yosh < 60` ni birinchi yozsak, 5 yoshli bola ham 40 000 to'laydi.

## 5. Yetkazib berish narxi

**Masala.** Shunday dastur yozing: posilka og'irligini (butun son, kg) so'raydi va yetkazib berish narxini chiqaradi:

- 1 kg va undan yengil — 15 000 so'm;
- 1 kg dan og'ir, lekin 5 kg dan oshmasa — 30 000 so'm;
- 5 kg dan og'ir — 50 000 so'm.

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

    Fayl: [p5.py](../../../downloads/dasturlash/week-03/p5.py)

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

    Fayl: [p6.py](../../../downloads/dasturlash/week-03/p6.py)

    **Tushuntirish.**

    - Ko'p `elif` ketma-ketligi: har bir raqam alohida tekshiriladi, tegishli blok topilganda qolganlari tekshirilmaydi.
    - `oy == 3` — son bilan taqqoslash; `oy` `int()` bilan songa aylantirilgan. Agar `int()` bo'lmasa, `"3" == 3` `False` bo'lar edi, chunki matn va son — har xil turlar.
    - Oxirgi `else` — "himoya" vazifasini bajaradi: `0`, `13`, `-5` kabi noto'g'ri qiymatlarni ushlaydi. Foydalanuvchi kiritishi mumkin bo'lgan **barcha** holatlarni o'ylab ko'rish yaxshi odat.
    - Bunday uzun zanjir ishlaydi, ammo takrorlanuvchi. Bitta o'zgaruvchining aniq qiymatlari tekshirilganda [`match`](lecture.md#match) qulayroq — keyingi masalada shu usul ishlatiladi.

## 7. Hafta kuni

**Masala.** Shunday dastur yozing: kun raqamini (1–7) so'raydi va `match` yordamida hafta kuni nomini chiqaradi. Boshqa raqam uchun "Bunday kun yo'q" deb javob beradi.

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

    match kun:
        case 1:
            print("Dushanba")
        case 2:
            print("Seshanba")
        case 3:
            print("Chorshanba")
        case 4:
            print("Payshanba")
        case 5:
            print("Juma")
        case 6:
            print("Shanba")
        case 7:
            print("Yakshanba")
        case _:
            print("Bunday kun yo'q")
    ```

    Fayl: [p7.py](../../../downloads/dasturlash/week-03/p7.py)

    **Tushuntirish.**

    - `match kun:` — `kun` qiymati har bir `case` bilan yuqoridan pastga solishtiriladi; birinchi mos kelgan `case` bloki bajariladi.
    - `case _:` — hech bir variantga mos kelmaganda ishlaydi (`else` kabi) va `0`, `8` kabi noto'g'ri qiymatlarni ushlaydi.
    - Natija 6-masaladagi `elif` zanjiri bilan bir xil, lekin `kun ==` har qatorda takrorlanmaydi.
    - Chegaralarni sinang: `1` (Dushanba), `7` (Yakshanba), `0` va `8` (xato qiymatlar).
    - `match` Python 3.10 dan boshlab mavjud.

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

    Fayl: [p8.py](../../../downloads/dasturlash/week-03/p8.py)

    **Tushuntirish.**

    - `and` — **mantiqiy "va"**: ikkala shart ham `True` bo'lsa, natija `True`. `a >= b and a >= c` — "`a` `b` dan ham, `c` dan ham kichik emas".
    - Birinchi shart `False` bo'lsa, `b` yoki `c` `a` dan katta, demak eng kattasi shu ikkisidan biri. Ularni tanlash uchun bitta taqqoslash — `b >= c` — yetarli: `True` bo'lsa `b`, aks holda `c`.
    - `>=` ishlatilgani uchun teng sonlar ham to'g'ri ishlaydi: `7, 7, 2` → `7`; `4, 4, 4` → `4`.

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

    Fayl: [p9.py](../../../downloads/dasturlash/week-03/p9.py)

    **Tushuntirish.**

    - Matnlar ham `==` bilan solishtiriladi: `o1 == o2` ikkala o'yinchi bir xil narsa tanlaganini tekshiradi → durang.
    - Birinchi o'yinchi yutadigan uchta holat: tosh qaychini, qaychi qog'ozni, qog'oz toshni yengadi. Ularning har biri `and` bilan yoziladi: ikkala o'yinchining tanlovi **bir vaqtda** mos kelishi kerak.
    - `else` — qolgan holatlar: durang ham emas, birinchi o'yinchi ham yutmagan → ikkinchi o'yinchi yutdi.
    - Matn solishtirish **katta-kichik harfni va aniq belgilarni** hisobga oladi: `Tosh` yoki `tosh ` (oxirida probel bilan) kiritilsa, shart bajarilmaydi. `qog'oz` dagi apostrof ham aynan shunday yozilishi kerak. Kiritilgan matnni `.strip().lower()` bilan tozalash yaxshi usul.
    - Dastur noto'g'ri so'zlarni tekshirmaydi: masalan, `tosh` va `salom` kiritilsa ham, `else` ishlaydi va "2-o'yinchi yutdi" chiqadi.

## 10. Parol tekshiruvi

**Masala.** Shunday dastur yozing: parolni so'raydi. Parol `42`, `qirq ikki` yoki `qirq-ikki` bo'lsa (harf registridan qat'i nazar), "To'g'ri parol", aks holda "Noto'g'ri parol" deb javob beradi.

Namuna:

```text
Parol? 42
To'g'ri parol
```

```text
Parol? Qirq Ikki
To'g'ri parol
```

```text
Parol? 12345
Noto'g'ri parol
```

??? success "Yechim"

    ```python
    parol = input("Parol? ").lower()

    if parol == "42":
        print("To'g'ri parol")
    elif parol == "qirq ikki" or parol == "qirq-ikki":
        print("To'g'ri parol")
    else:
        print("Noto'g'ri parol")
    ```

    Fayl: [p10.py](../../../downloads/dasturlash/week-03/p10.py)

    **Tushuntirish.**

    - `.lower()` — kiritilgan matnni kichik harflarga o'tkazadi, shuning uchun `Qirq Ikki`, `QIRQ IKKI` va `qirq ikki` bir xil hisoblanadi.
    - `or` — **mantiqiy "yoki"**: ikki shartdan kamida bittasi `True` bo'lsa, natija `True`. Parolning ikki yozilishidan istalgani qabul qilinadi.
    - `parol == "42"` — bu yerda `"42"` **matn**, chunki `input()` matn qaytaradi. `parol == 42` `False` bo'lardi.
    - Odatiy xato: `parol == "qirq ikki" or "qirq-ikki"` yozish. Bu **har doim** `True` bo'ladi, chunki bo'sh bo'lmagan satr Python'da `True` hisoblanadi ([ma'ruzaga qarang](lecture.md#bool)). Har bir taqqoslashni to'liq yozing: `parol == "a" or parol == "b"`.
    - Ikkala to'g'ri variantda ham bir xil xabar chiqadi; shartlarni `or` bilan birlashtirib, bitta `if` ga ham yozish mumkin edi.

## 11. Salomga mukofot

**Masala.** Shunday dastur yozing: "Yaxshimisan?" deb so'raydi. Javob "assalom" bilan boshlansa — "Mana senga $100", "salom" bilan boshlansa — "Mana senga $20", aks holda "Ha, zo'r!" deb javob beradi.

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
Ha, zo'r!
```

??? success "Yechim"

    ```python
    salom = input("Yaxshimisan? ").lower()

    if salom.startswith("assalom"):
        print("Mana senga $100")
    elif salom.startswith("salom"):
        print("Mana senga $20")
    else:
        print("Ha, zo'r!")
    ```

    Fayl: [p11.py](../../../downloads/dasturlash/week-03/p11.py)

    **Tushuntirish.**

    - `satr.startswith(boshi)` — satr berilgan matn bilan **boshlansa** `True`, aks holda `False` qaytaradi. `"assalomu alaykum".startswith("assalom")` → `True`.
    - Shuning uchun `Assalomu alaykum`, `Assalom!` yoki `assalom` — barchasi mos keladi: butun so'zni emas, faqat boshlanishini tekshiramiz.
    - `.lower()` ni zanjirda oldindan chaqirib, `Salom` va `SALOM` ni ham ushlaymiz.
    - Uning juft metodi ham bor: `satr.endswith(oxiri)` satr berilgan matn bilan **tugashini** tekshiradi. Uni 15-masalada ko'ramiz.
    - `startswith` `True` / `False` qaytargani uchun u to'g'ridan-to'g'ri `if` / `elif` ichida ishlatiladi.

## 12. Oddiy kalkulyator

**Masala.** Shunday dastur yozing: "son amal son" ko'rinishidagi ifodani (masalan, `3 + 4`) oladi va natijani chiqaradi. Nolga bo'lishda va noma'lum amalda xabar beradi.

Namuna:

```text
Amal: 3 + 4
Natija: 7.0
```

```text
Amal: 10 / 4
Natija: 2.5
```

```text
Amal: 5 / 0
0 ga bo'lib bo'lmaydi!
```

```text
Amal: 5 ^ 2
Bunday amal yo'q!
```

??? success "Yechim"

    ```python
    a, amal, b = input("Amal: ").split()

    a = float(a)
    b = float(b)

    if amal == "+":
        print("Natija:", a + b)
    elif amal == "-":
        print("Natija:", a - b)
    elif amal == "*":
        print("Natija:", a * b)
    elif amal == "/":
        if b == 0:
            print("0 ga bo'lib bo'lmaydi!")
        else:
            print("Natija:", a / b)
    else:
        print("Bunday amal yo'q!")
    ```

    Fayl: [p12.py](../../../downloads/dasturlash/week-03/p12.py)

    **Tushuntirish.**

    - `a, amal, b = input("Amal: ").split()` — kiritilgan satr bo'sh joylar bo'yicha uch bo'lakka ajratiladi: `"3 + 4"` → `"3"`, `"+"`, `"4"`. Ular mos ravishda `a`, `amal`, `b` ga saqlanadi. Shuning uchun foydalanuvchi sonlar va amalni **probellar bilan** yozishi shart: `3+4` (probelsiz) xato beradi (`ValueError`).
    - `a = float(a)`, `b = float(b)` — sonlar `float` ga aylantiriladi, shunda butun va kasr sonlar bilan ishlaydi. Amal belgisi `amal` matn bo'lib qoladi.
    - Har bir `elif` amal belgisini matn sifatida tekshiradi: `amal == "-"`.
    - **Ichma-ich shart.** `/` tarmog'ida yana bir `if` bor: avval `b == 0` tekshiriladi, shundagina bo'lish bajariladi. Nolga bo'lishning oldini olish uchun shu zarur.
    - Natija `float` bo'lgani uchun `3 + 4` → `7.0` chiqadi.
    - `else` — noma'lum amal (`^`, `%` va boshqalar) uchun.

## 13. Valyuta ayirboshlash

**Masala.** Bank dollarni 12 010 so'mdan sotadi va 11 500 so'mdan sotib oladi. Shunday dastur yozing: menyu ko'rsatadi va tanlov bo'yicha hisoblaydi:

- `1` — dollar sotib olish: foydalanuvchi so'm miqdorini kiritadi, dastur unga necha butun dollar berilishini chiqaradi;
- `2` — dollar sotish: foydalanuvchi dollar miqdorini kiritadi, dastur unga necha so'm berilishini chiqaradi;
- boshqa tanlov uchun "Bunday tanlov yo'q." deb javob beradi.

Namuna:

```text
Dollar sotib olish uchun 1 ni bosing.
Dollar sotish uchun 2 ni bosing.
Tanlov? 1
Qancha so'mingiz bor? 120100
Siz 10 dollar olasiz. Kurs: 12010
```

```text
Dollar sotib olish uchun 1 ni bosing.
Dollar sotish uchun 2 ni bosing.
Tanlov? 2
Necha dollar sotasiz? 10
Siz 115000 so'm olasiz. Kurs: 11500
```

```text
Dollar sotib olish uchun 1 ni bosing.
Dollar sotish uchun 2 ni bosing.
Tanlov? 3
Bunday tanlov yo'q.
```

??? success "Yechim"

    ```python
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
    ```

    Fayl: [p13.py](../../../downloads/dasturlash/week-03/p13.py)

    **Tushuntirish.**

    - Ikki kurs bor: foydalanuvchi dollar **sotib olganda** bank yuqori kursda (`sotish_kursi`) sotadi, foydalanuvchi dollar **sotganda** bank past kursda (`olish_kursi`) sotib oladi. Har bir tarmoq o'z kursidan foydalanadi va aynan shu kursni chiqaradi.
    - `\n` — matn ichidagi **yangi qator** belgisi. Shuning uchun bitta `print()` ikki qatorni chiqaradi.
    - `tanlov = input("Tanlov? ")` — tanlov **matn** sifatida saqlanadi. Shuning uchun taqqoslash `tanlov == "1"` (tirnoq bilan); `tanlov == 1` hech qachon `True` bo'lmaydi.
    - `som // sotish_kursi` — butun bo'lish: bank faqat to'liq dollar beradi. `round()` ishlatilsa, `126 000` so'm uchun `10.49...` → `10`, lekin `126 200` so'm uchun `10.5...` → `11` dollar chiqib, foydalanuvchi to'lamagan pulni olgan bo'lardi. Ortib qolgan so'mni `som % sotish_kursi` bilan topish mumkin.
    - Kurslar dastur boshida o'zgaruvchilarga saqlangan. Kurs o'zgarsa, faqat shu ikki qatorni o'zgartirish kifoya.

## 14. Ovqat vaqti

**Masala.** Shunday dastur yozing: soatni `soat:daqiqa` ko'rinishida (masalan, `7:30`) oladi va nonushta (7:00–8:00), tushlik (12:00–13:00) yoki kechki ovqat (18:00–19:00) vaqti ekanini aytadi, aks holda "Ishlaymiz!" deydi. Har bir oraliqning ikkala chegarasi ham shu oraliqqa kiradi.

Namuna:

```text
Soat necha bo'ldi? 7:30
Nonushta vaqti!
```

```text
Soat necha bo'ldi? 13:00
Tushlik vaqti!
```

```text
Soat necha bo'ldi? 9:15
Ishlaymiz!
```

??? success "Yechim"

    ```python
    def main():
        vaqt = input("Soat necha bo'ldi? ")

        vaqt = soatga_aylantir(vaqt)

        if vaqt >= 7.0 and vaqt <= 8.0:
            print("Nonushta vaqti!")
        elif vaqt >= 12.0 and vaqt <= 13.0:
            print("Tushlik vaqti!")
        elif vaqt >= 18.0 and vaqt <= 19.0:
            print("Kechki ovqat vaqti!")
        else:
            print("Ishlaymiz!")


    def soatga_aylantir(vaqt):
        soat, daqiqa = vaqt.split(":")

        return float(soat) + float(daqiqa) / 60


    main()
    ```

    Fayl: [p14.py](../../../downloads/dasturlash/week-03/p14.py)

    **Tushuntirish.**

    - `vaqt.split(":")` — satrni `:` belgisi bo'yicha bo'ladi: `"7:30".split(":")` → `["7", "30"]`. Argument sifatida ajratgich beriladi (argumentsiz `split()` bo'sh joy bo'yicha bo'ladi).
    - `soat, daqiqa = ...` — ro'yxat elementlari ikki o'zgaruvchiga ochiladi.
    - `float(soat) + float(daqiqa) / 60` — vaqtni **soat birligida** bitta songa aylantiradi: `7:30` → `7 + 30/60` = `7.5`. Shunday qilib vaqtni oddiy son sifatida solishtirish mumkin.
    - `return` — hisoblangan sonni `main()` ga qaytaradi. `vaqt = soatga_aylantir(vaqt)` da `vaqt` matndan songa o'zgaradi.
    - `vaqt >= 7.0 and vaqt <= 8.0` — **oraliq** tekshiruvi: ikkala shart ham `True` bo'lishi kerak. Python'da buni qisqa yozish ham mumkin: `7.0 <= vaqt <= 8.0`.
    - Chegaralar: `<=` tufayli `8:00`, `13:00` va `19:00` hali ovqat vaqtiga kiradi, `8:01` esa — "Ishlaymiz!".
    - Vaqt `soat:daqiqa` ko'rinishida kiritilishi shart; ikki nuqtasiz kiritilsa, `ValueError` chiqadi.

## 15. Ismni ajratib olish

**Masala.** Shunday dastur yozing: ism va familiyani (istalgan tartibda) oladi va faqat ismga salom beradi. Familiya `ov` yoki `ova` bilan tugaydi deb hisoblang.

Namuna:

```text
Ism va familiyangiz? karimov ali
Salom, Ali
```

```text
Ism va familiyangiz? dilnoza yusupova
Salom, Dilnoza
```

```text
Ism va familiyangiz? g'ulomov o'tkir
Salom, O'tkir
```

??? success "Yechim"

    ```python
    import string


    def main():
        toliq_ism = string.capwords(input("Ism va familiyangiz? "))

        print(f"Salom, {ism_ajratish(toliq_ism)}")


    def ism_ajratish(toliq_ism):
        birinchi, ikkinchi = toliq_ism.split()

        if birinchi.endswith("ov") or birinchi.endswith("ova"):
            return ikkinchi

        return birinchi


    main()
    ```

    Fayl: [p15.py](../../../downloads/dasturlash/week-03/p15.py)

    **Tushuntirish.**

    - `string.capwords(...)` — har bir so'z bosh harf bilan boshlanadi (`karimov ali` → `Karimov Ali`). `.title()` dan farqli o'laroq, o'zbekcha ismlarni buzmaydi: `g'ulomov` → `G'ulomov` ([2-hafta ma'ruzasiga qarang](../week-02/lecture.md#satrlar-bilan-ishlash)).
    - `birinchi, ikkinchi = toliq_ism.split()` — to'liq ism ikki so'zga ajratiladi va ikki o'zgaruvchiga saqlanadi.
    - `satr.endswith(oxiri)` — satr berilgan matn bilan **tugasa** `True` qaytaradi. `"Karimov".endswith("ov")` → `True`.
    - `birinchi.endswith("ov") or birinchi.endswith("ova")` — birinchi so'z familiyaga o'xshasa (`ov` yoki `ova` bilan tugasa), ism ikkinchi so'z bo'ladi.
    - **Erta `return`.** `return ikkinchi` bajarilishi bilan funksiya **darhol tugaydi**; keyingi qator (`return birinchi`) bajarilmaydi. Shart `False` bo'lsa, `if` bloki o'tkazib yuboriladi va `return birinchi` ishlaydi. Shuning uchun bu yerda `else` yozish shart emas.
    - `print(f"Salom, {ism_ajratish(toliq_ism)}")` — f-string ichida funksiya chaqiruvini ham yozish mumkin: funksiya qaytargan qiymat shu joyga qo'yiladi.
    - **Cheklovlar.** Dastur aynan ikki so'zni kutadi; boshqa son kiritilsa `ValueError` chiqadi. `ov`/`ova` bilan tugamaydigan familiyalar (masalan, `Aliyev`) bo'lsa, tartib noto'g'ri aniqlanadi: `Aliyev Vali` → `Salom, Aliyev`.

## 16. To'rtburchak yuzi

**Masala.** Shunday funksiya yozing: to'rtburchakning uzunligi va enini parametr sifatida oladi va yuzini ekranga chiqaradi. Uzunlik va enni foydalanuvchidan so'rang.

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

    Fayl: [p16.py](../../../downloads/dasturlash/week-03/p16.py)

    **Tushuntirish.**

    - `def yuza(uzunlik, eni):` — ikki **parametrli** funksiya. `yuza(a, b)` chaqirilganda `a` qiymati `uzunlik` ga, `b` qiymati `eni` ga **tartib bo'yicha** o'tadi.
    - Funksiya e'lon qilinishi (`def`) uni **ishga tushirmaydi**; faqat `yuza(a, b)` qatori chaqirganda ishlaydi.
    - Funksiya ichida `return` yo'q: natija ekranga chiqariladi, lekin qaytarilmaydi (`None`). Natijani keyinchalik ishlatmoqchi bo'lsak (masalan, `yuza(5, 3) * 2`), `print` o'rniga `return uzunlik * eni` yozish kerak ([ma'ruzaga qarang](lecture.md#return-natijani-qaytarish)).
    - `uzunlik` va `eni` — funksiyaning **local** o'zgaruvchilari, ular faqat funksiya ichida mavjud; `a` va `b` esa funksiyadan tashqarida yaratilgan **global** o'zgaruvchilar ([scope](lecture.md#scope-ozgaruvchi-qayerda-korinadi)).

## Qisqa lug'at

| Tushuncha | Ma'nosi |
|---|---|
| `if` / `elif` / `else` | shart bo'yicha tarmoqlanish; sharti `True` bo'lgan birinchi blok bajariladi |
| `match` / `case` | bitta qiymatning aniq variantlari bo'yicha tarmoqlanish; `case _` — qolgan holatlar |
| `==`, `!=`, `>`, `<`, `>=`, `<=` | taqqoslash operatorlari (natijasi `True` / `False`) |
| `and`, `or`, `not` | mantiqiy "va", "yoki", "emas" |
| `satr.startswith(x)` / `endswith(x)` | satr `x` bilan boshlansa / tugasa `True` |
| `satr.split(ajratgich)` | satrni ajratgich bo'yicha bo'laklarga bo'ladi |
| local / global | funksiya ichidagi / fayl darajasidagi o'zgaruvchi |
