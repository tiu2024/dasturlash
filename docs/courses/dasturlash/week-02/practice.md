# Amaliyot

Bu sahifada [ma'ruzada](lecture.md) o'rganilgan vositalar bilan darsda yechilgan 11 ta masala keltirilgan. Har bir masala shartidan keyin **Yechim** bloki joylashgan: u yopiq turadi, ustiga bosib oching. Avval masalani o'zingiz yechib ko'ring va natijani namuna bilan solishtiring, keyin yechim va tushuntirishni o'qing.

Har bir yechim ichida shu dasturning `.py` fayliga havola bor.

!!! note "Funksiyalar"
    4, 6 va 11-masalalarda o'zimiz yozgan funksiyalar (`def`, `return`) ishlatiladi. Bu yerda ular qisqa tushuntirilgan; batafsil tushuntirish [3-hafta ma'ruzasida](../week-03/lecture.md#funksiyalar).

## 1. Salomlashish

**Masala.** Shunday dastur yozing: foydalanuvchining ismini so'rab, unga salom beradi.

Namuna:

```text
Ismingiz nima? Ali
Salom, Ali
```

??? success "Yechim"

    ```python
    ism = input("Ismingiz nima? ")
    print(f"Salom, {ism}")
    ```

    Fayl: [p1.py](../../../downloads/dasturlash/week-02/p1.py)

    **Tushuntirish.**

    - `input("Ismingiz nima? ")` ekranga savolni chiqaradi, foydalanuvchi yozib `Enter` bosguncha kutadi va yozilgan **matnni** qaytaradi.
    - `ism = ...` — qaytgan matn `ism` o'zgaruvchisiga saqlanadi.
    - `f"Salom, {ism}"` — f-string: `{ism}` o'rniga o'zgaruvchining qiymati qo'yiladi.
    - Foydalanuvchi `ali` deb yozsa, dastur ham `Salom, ali` deydi: matn o'zgartirilmaydi. Keyingi dastur shuni tuzatadi.

## 2. Ismni tozalash va bosh harfga o'tkazish

**Masala.** Shunday dastur yozing: ismdagi ortiqcha bo'sh joylarni olib tashlaydi va har bir so'zni bosh harf bilan boshlaydi. O'zbekcha ismlar (`o'tkir`, `g'ayrat`) ham to'g'ri chiqishi kerak.

Namuna:

```text
Ismingiz nima?   aziza karimova 
Salom, Aziza Karimova
```

```text
Ismingiz nima? o'tkir g'ulomov
Salom, O'tkir G'ulomov
```

??? success "Yechim"

    ```python
    import string

    ism = input("Ismingiz nima? ").strip()
    ism = string.capwords(ism)
    print(f"Salom, {ism}")
    ```

    Fayl: [p2.py](../../../downloads/dasturlash/week-02/p2.py)

    **Tushuntirish.**

    - `.strip()` — satrning **boshi va oxiridagi** bo'sh joylarni (probel, tabulyatsiya, qator oxiri) olib tashlaydi. O'rtadagi bo'sh joylarga tegmaydi.
    - `input(...).strip()` — **zanjir**: avval `input()` matn qaytaradi, keyin `.strip()` shu matnni tozalaydi.
    - `string.capwords(ism)` — har bir so'zning birinchi harfini katta, qolganlarini kichik qiladi: `aziza karimova` → `Aziza Karimova`. U so'zlar orasidagi ortiqcha bo'sh joylarni ham bittaga qisqartiradi. `import string` qatori shu funksiyani ulaydi ([ma'ruzaga qarang](lecture.md#satrlar-bilan-ishlash)).
    - Nega `.title()` emas: `.title()` tutuq belgisidan keyingi harfni ham katta qiladi: `"o'tkir".title()` → `"O'Tkir"`. `capwords` esa `O'tkir` beradi.
    - Satr metodlari va funksiyalari **yangi satr qaytaradi**, eskisini o'zgartirmaydi (Python satrlari o'zgarmasdir). Shuning uchun natijani `ism = ...` ga qayta saqlaymiz.

## 3. Ism va familiyani ajratish

**Masala.** Shunday dastur yozing: foydalanuvchi ism va familiyasini bitta qatorda yozadi; dastur ularni ikkita o'zgaruvchiga ajratadi va faqat ismga salom beradi.

Namuna:

```text
Ismingiz nima? aziza karimova
Salom, Aziza
```

??? success "Yechim"

    ```python
    ism, familiya = input("Ismingiz nima? ").strip().split()

    ism = ism.capitalize()

    print(f"Salom, {ism}")
    # print(f"Salom, {ism.capitalize()}")
    ```

    Fayl: [p3.py](../../../downloads/dasturlash/week-02/p3.py)

    **Tushuntirish.**

    - `.split()` — satrni bo'sh joylar bo'yicha bo'laklarga ajratib, **ro'yxat** qaytaradi: `"aziza karimova".split()` → `["aziza", "karimova"]` ([ma'ruzaga qarang](lecture.md#satrlar-bilan-ishlash)). Argumentsiz chaqirilsa, ketma-ket bir nechta bo'sh joy ham bitta ajratgich hisoblanadi.
    - `ism, familiya = [...]` — **ochib o'zlashtirish** (*unpacking*): ro'yxatning birinchi elementi `ism` ga, ikkinchisi `familiya` ga tushadi. Elementlar soni o'zgaruvchilar soniga **aniq teng** bo'lishi shart.
    - `ism = ism.capitalize()` — bitta so'zning birinchi harfini katta qiladi va qiymatni o'zgaruvchining o'ziga qayta saqlaydi. `.capitalize()` o'zbekcha ismlarni ham to'g'ri yozadi: `"o'tkir"` → `"O'tkir"`.
    - `#` bilan boshlangan oxirgi qator — izoh. U ishlamaydi, lekin bir xil natijaga boshqa yo'l bilan erishish mumkinligini ko'rsatadi: `{ism.capitalize()}` ni f-string ichida to'g'ridan-to'g'ri chaqirish.
    - **Cheklov.** Foydalanuvchi bitta so'z (`aziza`) yoki uch so'z (`aziza karimova qizi`) yozsa, dastur `ValueError` bilan to'xtaydi. Sabab: `split()` ikkitadan boshqa sondagi bo'lak qaytardi. Bunday holatlarni [shartlar](../week-03/lecture.md#shartlar) bilan boshqarishni 3-haftada o'rganamiz.
    - `familiya` o'zgaruvchisi hozir ishlatilmayapti: u faqat ikkinchi so'zni "ushlab turish" uchun kerak.

## 4. Funksiya bilan salomlashish

**Masala.** Shunday dastur yozing: salomlashish kodini funksiyaga ajratib, ikki marta ishlatadi.

Namuna:

```text
Ismingiz nima? ali valiyev
Salom, Ali Valiyev
Ismingiz nima? SARDOR
Salom, Sardor
```

??? success "Yechim"

    ```python
    import string


    def salom(ism="Do'stlarga"):
        ism = string.capwords(ism)
        print(f"Salom, {ism}")


    def main():
        ism1 = input("Ismingiz nima? ")
        salom(ism1)

        ism2 = input("Ismingiz nima? ")
        salom(ism2)


    main()
    ```

    Fayl: [p4.py](../../../downloads/dasturlash/week-02/p4.py)

    **Tushuntirish.**

    - `def` — o'zimizning **funksiyamizni** yaratadi. `def salom(ism="Do'stlarga"):` ning ostidagi **chekinish** (4 ta bo'sh joy) funksiya tanasini bildiradi.
    - `ism` — funksiyaning **parametri**: funksiya chaqirilganda unga berilgan qiymatni oladi. `salom(ism1)` da `ism1` — **argument**.
    - `ism="Do'stlarga"` — parametrning **standart qiymati**. Funksiya argumentsiz chaqirilsa (`salom()`), shu qiymat ishlatiladi: `Salom, Do'stlarga`. Bu dasturda funksiya doim argument bilan chaqirilgani uchun standart qiymat ishlatilmaydi.
    - Funksiya **chaqirilmaguncha** ishlamaydi: `def` uni faqat yaratadi. Ishga tushirish uchun oxirida `main()` chaqiriladi. `main()` — dasturning asosiy qismini jamlash uchun odatiy nom.
    - Foyda: salomlashish mantiqi (`capwords` va `print`) bir marta yozildi, ikki marta ishlatildi.
    - `salom()` ichida `return` yo'q: u natijani ekranga **chiqaradi**, lekin hech narsa **qaytarmaydi** (natijasi `None`). `print` va `return` farqi — 6-masalada va [3-hafta ma'ruzasida](../week-03/lecture.md#return-natijani-qaytarish).

## 5. Ikki son ustida amallar

**Masala.** Shunday dastur yozing: ikki butun son oladi va barcha asosiy arifmetik amallar natijasini chiqaradi.

Namuna (`X = 17`, `Y = 5`):

```text
X + Y = 22
X - Y = 12
X * Y = 85
X / Y = 3.4
X // Y = 3
X % Y = 2
X ** Y = 1419857
```

??? success "Yechim"

    ```python
    x = int(input("X: "))
    y = int(input("Y: "))

    natija = x + y
    print("X + Y =", natija)

    natija = x - y
    print("X - Y =", natija)

    natija = x * y
    print("X * Y =", natija)

    natija = x / y
    print("X / Y =", natija)

    natija = x // y
    print("X // Y =", natija)

    natija = x % y
    print("X % Y =", natija)

    natija = x ** y
    print("X ** Y =", natija)
    ```

    Fayl: [p5.py](../../../downloads/dasturlash/week-02/p5.py)

    **Tushuntirish.**

    - `int(input(...))` — `input()` matn qaytaradi, `int()` esa uni butun songa aylantiradi. Aks holda `x + y` sonlarni qo'shmasdan, matnlarni ulab yuborardi (`"17" + "5"` → `"175"`).
    - `natija` o'zgaruvchisi har safar yangi qiymat oladi; eskisi yo'qoladi, lekin biz uni chiqarib bo'lgan edik.
    - `print("X + Y =", natija)` — vergul bilan ajratilgan qiymatlar orasiga `print` o'zi **bitta bo'sh joy** qo'yadi, shuning uchun `"X + Y ="` matni oxiriga bo'sh joy yozilmaydi.
    - `/` natijasi har doim `float` (`3.4`); `//` — butun bo'lish, natijani pastga yaxlitlaydi (`17 // 5` → `3`); `%` — qoldiq (`17 % 5` → `2`); `**` — daraja (`17 ** 5`). Python'da daraja `^` bilan emas, `**` bilan yoziladi.
    - `ZeroDivisionError`: `Y = 0` kiritilsa, `/`, `//` va `%` amallarida dastur to'xtaydi, chunki nolga bo'lib bo'lmaydi.

## 6. Kvadrat hisoblash

**Masala.** Shunday dastur yozing: butun va kasr sonlarning kvadratini funksiya yordamida hisoblaydi.

Namuna:

```text
Butun son: 7
Kasr son: 2.5
7 ning kvadrati = 49
2.5 ning kvadrati = 6.25
```

??? success "Yechim"

    ```python
    def kvadrat(x):
        return x ** 2


    def main():
        butun_son = int(input("Butun son: "))
        kasr_son = float(input("Kasr son: "))

        print(f"{butun_son} ning kvadrati = {kvadrat(butun_son)}")
        print(f"{kasr_son} ning kvadrati = {kvadrat(kasr_son)}")


    main()
    ```

    Fayl: [p6.py](../../../downloads/dasturlash/week-02/p6.py)

    **Tushuntirish.**

    - `return` — funksiyadan **natijani qaytaradi**: `print` qiymatni ekranga chiqaradi, `return` esa uni chaqirgan joyga beradi. Batafsil — [3-hafta ma'ruzasida](../week-03/lecture.md#return-natijani-qaytarish).
    - `return x ** 2` bajarilganda funksiya **darhol tugaydi**, `kvadrat(7)` ifodasi esa `49` ga aylanadi, go'yo kodda `49` yozilgandek. Shuning uchun uni f-string `{ }` ichiga to'g'ridan-to'g'ri yozish mumkin.
    - Taqqoslang: funksiya ichida `return x ** 2` o'rniga `print(x ** 2)` yozilsa, ekranga avval son alohida qatorda chiqadi, keyin f-string ichida `None` ko'rinadi: `7 ning kvadrati = None`.
    - Bitta funksiya ham `int`, ham `float` bilan ishlaydi: `7 ** 2` → `49` (`int`), `2.5 ** 2` → `6.25` (`float`).
    - `int(input(...))` va `float(input(...))` — kiritilgan matnni mos songa aylantiradi. `int` ga `"2.5"` kiritsangiz, `ValueError` chiqadi.

## 7. Kichik harfga o'tkazish

**Masala.** Shunday dastur yozing: xabarni to'liq kichik harflarda chiqaradi.

Namuna:

```text
Nima? SaLoM DuNyo
salom dunyo
```

??? success "Yechim"

    ```python
    xabar = input("Nima? ")

    xabar = xabar.lower()
    print(xabar)
    ```

    Fayl: [p7.py](../../../downloads/dasturlash/week-02/p7.py)

    **Tushuntirish.**

    - `.lower()` — satrdagi barcha harflarni kichik harfga o'tkazadi. Teskarisi — `.upper()`.
    - `string.capwords()` bilan farqi: `capwords` har so'zni bosh harfdan boshlaydi, `lower()` hamma harfni kichik qiladi.
    - `input("Nima? ")` da savol oxiridagi probel muhim: u foydalanuvchi yozgan matnni savoldan ajratib turadi. Probel bo'lmasa, matn savolga yopishib qoladi (`Nima?salom`).
    - Natija qayta `xabar` ga saqlanadi, chunki `lower()` yangi satr qaytaradi.

## 8. Bo'sh joylarni almashtirish

**Masala.** Shunday dastur yozing: xabardagi har bir bo'sh joyni `...` bilan almashtiradi.

Namuna:

```text
Nima? Men Python o'rganyapman
Men...Python...o'rganyapman
```

??? success "Yechim"

    ```python
    xabar = input("Nima? ")

    xabar = xabar.replace(" ", "...")

    print(xabar)
    ```

    Fayl: [p8.py](../../../downloads/dasturlash/week-02/p8.py)

    **Tushuntirish.**

    - `satr.replace(eski, yangi)` — satrdagi `eski` qismning **hamma** uchragan joyini `yangi` bilan almashtiradi ([ma'ruzaga qarang](lecture.md#satrlar-bilan-ishlash)).
    - Almashtiriladigan va yangi qism bir belgi bo'lishi shart emas: bu yerda bitta bo'sh joy uchta nuqtaga almashdi.
    - Agar `eski` qism topilmasa, satr o'zgarishsiz qaytadi.
    - `replace` katta-kichik harfni farqlaydi: `"a"` ni almashtirsangiz, `"A"` o'zgarmaydi.

## 9. Emoji'larga almashtirish

**Masala.** Shunday dastur yozing: matndagi `:)` va `:(` belgilarini emoji'ga o'zgartiradi.

Namuna:

```text
Nima gap? Zo'r :) lekin charchadim :(
Zo'r 😊 lekin charchadim 🙁
```

??? success "Yechim"

    ```python
    xabar = input("Nima gap? ")

    xabar = xabar.replace(":)", "😊")
    xabar = xabar.replace(":(", "🙁")

    print(xabar)
    ```

    Fayl: [p9.py](../../../downloads/dasturlash/week-02/p9.py)

    **Tushuntirish.**

    - Ikkita `replace()` ketma-ket qo'llanadi: birinchisi `:)` ni, ikkinchisi `:(` ni almashtiradi. Har biri oldingisining natijasi ustida ishlaydi.
    - Emoji ham oddiy Unicode belgi, shuning uchun uni satr ichiga yozish mumkin (1-haftadagi Unicode jadvalini eslang: 😀 — `U+1F600`).
    - Ba'zi terminallar emoji'ni ko'rsata olmasligi mumkin. Bunda dasturda xato yo'q, muammo terminalning shriftida yoki kodlashida bo'ladi.

## 10. Massadan energiyani hisoblash

**Masala.** Shunday dastur yozing: kilogrammda berilgan massaga mos energiyani Eynshteyn formulasi `E = m · c²` bo'yicha joulda hisoblaydi (`c` — yorug'lik tezligi, taxminan 300 000 000 m/s).

Namuna:

```text
Massa (kg): 2
E = 180000000000000000 J
```

??? success "Yechim"

    ```python
    c = 300_000_000

    m = float(input("Massa (kg): "))

    e = round(m * c ** 2)

    print(f"E = {e} J")
    ```

    Fayl: [p10.py](../../../downloads/dasturlash/week-02/p10.py)

    **Tushuntirish.**

    - `300_000_000` — raqamlar orasidagi `_` faqat o'qishni osonlashtiradi, qiymatga ta'sir qilmaydi ([ma'ruzaga qarang](lecture.md#malumot-turlari)).
    - `c` — qiymati o'zgarmaydigan **doimiy** (konstanta) sifatida ishlatilgan. Python buni majburlamaydi, lekin odatda bunday qiymatlarga qayta qiymat berilmaydi.
    - `float(input(...))` — massa kasr son bo'lishi mumkin (`0.5`).
    - `m * c ** 2` — formuladagi `m · c²`. `**` ustuvorligi `*` dan yuqori, shuning uchun avval `c ** 2` hisoblanadi, keyin `m` ga ko'paytiriladi. Qavs shart emas.
    - `round(x)` — sonni eng yaqin butun songa yaxlitlaydi ([ma'ruzaga qarang](lecture.md#natijani-chiroyli-chiqarish)). `float` ni `round` qilgach, natija `int` bo'ladi, shuning uchun natija `1.8e+17` ko'rinishida emas, kasrsiz yoziladi.

## 11. Choy puli (tip) hisoblash

**Masala.** Shunday dastur yozing: hisob summasi (`$` belgisi bilan) va foizni (`%` belgisi bilan) oladi va choy pulini hisoblaydi.

Namuna:

```text
Qancha bo'ldi? $50
Necha foiz? 15%
Tip: 7.50
```

??? success "Yechim"

    ```python
    def main():
        narx = narxga_aylantir(input("Qancha bo'ldi? "))
        foiz = foizga_aylantir(input("Necha foiz? "))

        tip = narx * foiz

        print(f"Tip: {tip:.2f}")


    def narxga_aylantir(n):
        n = n.strip("$")
        return float(n)


    def foizga_aylantir(f):
        f = f.strip("%")
        return float(f) / 100


    main()
    ```

    Fayl: [p11.py](../../../downloads/dasturlash/week-02/p11.py)

    **Tushuntirish.**

    - Dastur uch qismga bo'lingan: `main()` — asosiy oqim, `narxga_aylantir()` — summani songa aylantirish, `foizga_aylantir()` — foizni songa aylantirish. Har funksiya bitta ishni bajaradi.
    - Ikki yordamchi funksiya hech narsa chiqarmaydi: ular hisoblangan sonni `return` bilan `main()` ga **qaytaradi**. `narx = narxga_aylantir(input(...))` qatorida funksiya chaqiruvi qaytgan songa (`50.0`) almashadi. `return` bo'lmaganda `narx` ichida `None` bo'lardi va `narx * foiz` `TypeError` berardi.
    - Ma'lumot oqimi: `main` → argument → funksiya → `return` → `main`. `n` va `f` o'zgaruvchilari faqat o'z funksiyasi ichida mavjud ([scope](../week-03/lecture.md#scope-ozgaruvchi-qayerda-korinadi)).
    - `n.strip("$")` — `strip` ga argument berilsa, satrning **boshi va oxiridan** shu belgilarni olib tashlaydi: `"$50"` → `"50"`. Belgi bo'lmasa, satr o'zgarmaydi, shuning uchun `50` kiritilsa ham dastur ishlaydi.
    - `float("50")` → `50.0`. Matn faqat son shaklida bo'lgandagina `float()` ishlaydi; `"$50"` ni to'g'ridan-to'g'ri aylantirsak, `ValueError` chiqqan bo'lar edi.
    - `float(f) / 100` — foizni ulushga aylantiradi: `15` → `0.15`.
    - `tip = narx * foiz` → `50.0 * 0.15` = `7.5`.
    - `{tip:.2f}` — f-string formatlash: `.2f` natijani **ikki kasr raqami** bilan chiqaradi (`7.5` → `7.50`).
    - Yordamchi funksiyalar `main()` dan keyin yozilgan, lekin `main()` eng oxirida chaqirilgani uchun muammo yo'q: chaqiruv paytiga kelib hamma funksiya yaratilgan bo'ladi.

## Qisqa lug'at

| Tushuncha | Ma'nosi |
|---|---|
| `input(savol)` | savolni chiqarib, foydalanuvchi matnini qaytaradi |
| `satr.strip()`, `satr.strip(belgilar)` | boshi va oxiridagi bo'sh joylarni (yoki ko'rsatilgan belgilarni) olib tashlaydi |
| `string.capwords(satr)` | har so'zni bosh harf bilan boshlaydi (o'zbekcha `o'`, `g'` bilan ham to'g'ri) |
| `satr.capitalize()` | birinchi harfni katta, qolganini kichik qiladi |
| `satr.lower()` / `upper()` | hammasini kichik / hammasini katta qiladi |
| `satr.split()` | bo'sh joylar bo'yicha bo'lib, ro'yxat qaytaradi |
| `satr.replace(eski, yangi)` | barcha `eski` qismlarni `yangi` ga almashtiradi |
| `int()`, `float()` | matnni butun / kasr songa aylantiradi |
| `round(x)` | eng yaqin butun songa yaxlitlaydi |
| `def nom(parametr):` | funksiya yaratadi; `return` natija qaytaradi |
| `f"{qiymat:.2f}"` | qiymatni ikki kasr raqami bilan chiqaradi |
