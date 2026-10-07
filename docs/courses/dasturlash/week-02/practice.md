# Amaliyot

Bu sahifada [ma'ruzada](lecture.md) o'rganilgan vositalar bilan darsda yechilgan 11 ta masala keltirilgan. Har bir masala shartidan keyin **Yechim** bloki joylashgan: u yopiq turadi, ustiga bosib oching. Avval masalani o'zingiz yechib ko'ring va natijani namuna bilan solishtiring, keyin yechim va tushuntirishni o'qing.

Har bir yechim ichida shu dasturning `.py` fayliga havola bor.

## 1. Salomlashish

**Masala.** Shunday dastur yozing: foydalanuvchining ismini so'rab, unga salom beradi.

Namuna:

```text
Isming nma? Ali
Salom, Ali
```

??? success "Yechim"

    ```python
    ism = input("Isming nma? ")
    print(f"Salom, {ism}")
    ```

    Fayl: [p1.py](../../../downloads/dasturlash/week-02/p1.py)

    **Tushuntirish.**

    - `input("Isming nma? ")` ekranga savolni chiqaradi, foydalanuvchi yozib `Enter` bosguncha kutadi va yozilgan **matnni** qaytaradi.
    - `ism = ...` — qaytgan matn `ism` o'zgaruvchisiga saqlanadi.
    - `f"Salom, {ism}"` — f-string: `{ism}` o'rniga o'zgaruvchining qiymati qo'yiladi.
    - Foydalanuvchi `ali` deb yozsa, dastur ham `Salom, ali` deydi: matn o'zgartirilmaydi. Keyingi dastur shuni tuzatadi.

## 2. Ismni tozalash va bosh harfga o'tkazish

**Masala.** Shunday dastur yozing: ismdagi ortiqcha bo'sh joylarni olib tashlaydi va har bir so'zni bosh harf bilan boshlaydi.

Namuna:

```text
Isming nma?   aziza karimova 
Salom, Aziza Karimova
```

??? success "Yechim"

    ```python
    ism = input("Isming nma? ").strip().title()
    print(f"Salom, {ism}")
    ```

    Fayl: [p2.py](../../../downloads/dasturlash/week-02/p2.py)

    **Tushuntirish.**

    - `.strip()` — satrning **boshi va oxiridagi** bo'sh joylarni (probel, tabulyatsiya, qator oxiri) olib tashlaydi. O'rtadagi bo'sh joylarga tegmaydi.
    - `.title()` — har bir so'zning birinchi harfini katta, qolganlarini kichik qiladi: `aziza karimova` → `Aziza Karimova`.
    - Metodlar chapdan o'ngga ketma-ket bajariladi (**zanjir**): avval `input()` matn qaytaradi, keyin `strip()` uni tozalaydi, keyin `title()` natijani o'zgartiradi.
    - Satr metodlari **yangi satr qaytaradi**, eskisini o'zgartirmaydi (Python satrlari o'zgarmasdir). Shuning uchun natijani `ism = ...` ga qayta saqlaymiz.

## 3. Ism va familiyani ajratish

**Masala.** Shunday dastur yozing: foydalanuvchi ism va familiyasini bitta qatorda yozadi; dastur ularni ikkita o'zgaruvchiga ajratadi va faqat ismga salom beradi.

Namuna:

```text
Isming nma? aziza karimova
Salom, Aziza
```

??? success "Yechim"

    ```python
    ism, familiya = input("Isming nma? ").strip().split()

    ism = ism.title()

    print(f"Salom, {ism}")
    # print(f"Salom, {ism.title()}")
    ```

    Fayl: [p3.py](../../../downloads/dasturlash/week-02/p3.py)

    **Tushuntirish.**

    - `.split()` — satrni bo'sh joylar bo'yicha bo'laklarga ajratib, **ro'yxat** qaytaradi: `"aziza karimova".split()` → `["aziza", "karimova"]`. Argumentsiz chaqirilsa, ketma-ket bir nechta bo'sh joy ham bitta ajratgich hisoblanadi.
    - `ism, familiya = [...]` — **ochib o'zlashtirish** (*unpacking*): ro'yxatning birinchi elementi `ism` ga, ikkinchisi `familiya` ga tushadi. Elementlar soni o'zgaruvchilar soniga **aniq teng** bo'lishi shart.
    - `ism = ism.title()` — qiymatni o'zgaruvchining o'ziga qayta saqlash.
    - `#` bilan boshlangan oxirgi qator — izoh. U ishlamaydi, lekin bir xil natijaga boshqa yo'l bilan erishish mumkinligini ko'rsatadi: `{ism.title()}` ni f-string ichida to'g'ridan-to'g'ri chaqirish.
    - **Cheklov.** Foydalanuvchi bitta so'z (`aziza`) yoki uch so'z (`aziza karimova qizi`) yozsa, dastur `ValueError` bilan to'xtaydi. Sabab: `split()` ikkitadan boshqa son qaytardi. Bunday holatlarni shartlar (`if`) bilan boshqarishni keyingi haftalarda o'rganamiz.
    - `familiya` o'zgaruvchisi hozir ishlatilmayapti: u faqat ikkinchi so'zni "ushlab turish" uchun kerak.

## 4. Funksiya bilan salomlashish

**Masala.** Shunday dastur yozing: salomlashish kodini funksiyaga ajratib, ikki marta ishlatadi.

Namuna:

```text
Isming nma? ali valiyev
Salom, Ali Valiyev
Isming nma? SARDOR
Salom, Sardor
```

??? success "Yechim"

    ```python
    def salom(ism = "Dostlarga"):

        ism = ism.title()

        print(f"Salom, {ism}")

    def main():
        ism1 = input("Isming nma? ")
        salom(ism1)

        ism2 = input("Isming nma? ")
        salom(ism2)

    main()
    ```

    Fayl: [p4.py](../../../downloads/dasturlash/week-02/p4.py)

    **Tushuntirish.**

    - `def` — o'zimizning **funksiyamizni** yaratadi. `def salom(ism):` ning ostidagi **chekinish** (4 ta bo'sh joy) funksiya tanasini bildiradi.
    - `ism` — funksiyaning **parametri**: funksiya chaqirilganda unga berilgan qiymatni oladi. `salom(ism1)` da `ism1` — **argument**.
    - `ism = "Dostlarga"` — parametrning **standart qiymati**. Funksiya argumentsiz chaqirilsa (`salom()`), shu qiymat ishlatiladi: `Salom, Dostlarga`. Bu dasturda funksiya doim argument bilan chaqirilgani uchun standart qiymat ishlamaydi.
    - Funksiya **chaqirilmaguncha** ishlamaydi: `def` faqat uni "e'lon qiladi". Ishga tushirish uchun oxirida `main()` chaqiriladi.
    - `main()` — dasturning asosiy qismini jamlash uchun odatiy nom. Bu yerda `main` `salom` dan keyin e'lon qilingan, lekin ahamiyati yo'q: `main()` qatori oxirida chaqiriladi, shu paytga kelib ikkala funksiya ham tayyor bo'ladi.
    - Foyda: salomlashish mantiqi (`title()` va `print`) bir marta yozildi, ikki marta ishlatildi.
    - **`return` haqida.** `salom()` ichida `return` yo'q: u natijani ekranga **chiqaradi** (`print`), lekin hech narsa **qaytarmaydi**. Qaytarilgan qiymat bo'lmasa, Python funksiya natijasi sifatida maxsus `None` qiymatini beradi. Shuning uchun `x = salom("ali")` ekranga salom chiqaradi, lekin `x` ichida `None` bo'ladi. Qiymatni funksiyadan olib, keyin ishlatmoqchi bo'lsak, `return` kerak bo'ladi (keyingi 6-dasturga qarang).
    - Funksiyalarni 3-haftada batafsil o'rganamiz.

## 5. Ikki son ustida amallar

**Masala.** Shunday dastur yozing: ikki butun son oladi va barcha asosiy arifmetik amallar natijasini chiqaradi.

Namuna (`X = 17`, `Y = 5`):

```text
X + Y = 22
X - Y =  12
X * Y =  85
X / Y =  3.4
Qoldiqsiz: X / Y =  3
X ^ Y =  1419857
```

??? success "Yechim"

    ```python
    x = int(input("X: "))
    y = int(input("Y: "))

    natija = x + y
    print("X + Y =", natija)

    natija = x - y
    print("X - Y = ", natija)

    natija = x * y
    print("X * Y = ", natija)

    natija = x / y
    print("X / Y = ", natija)

    natija = x // y
    print("Qoldiqsiz: X / Y = ", natija)

    natija = x ** y
    print("X ^ Y = ", natija)
    ```

    Fayl: [p5.py](../../../downloads/dasturlash/week-02/p5.py)

    **Tushuntirish.**

    - `int(input(...))` — `input()` matn qaytaradi, `int()` esa uni butun songa aylantiradi. Aks holda `x + y` sonlarni qo'shmasdan, matnlarni ulab yuborardi (`"17" + "5"` → `"175"`).
    - `natija` o'zgaruvchisi har safar yangi qiymat oladi; eskisi yo'qoladi, lekin biz uni chiqarib bo'lgan edik.
    - `print("X + Y =", natija)` — vergul bilan ajratilgan qiymatlar orasiga `print` **bitta bo'sh joy** qo'yadi. Shu sababli `"X - Y = "` oxiridagi bo'sh joy bilan birga ikki bo'sh joy chiqadi (natijada `=` dan keyin kengroq masofa).
    - `/` natijasi har doim `float` (`3.4`); `//` — butun bo'lish, natijani pastga yaxlitlaydi (`17 // 5` → `3`); `**` — daraja (`17 ** 5`).
    - `ZeroDivisionError`: `Y = 0` kiritilsa, `/` va `//` amallarida dastur to'xtaydi, chunki nolga bo'lib bo'lmaydi.
    - Matndagi `^` — oddiy yozuv belgisi; Python'da daraja `**` bilan yoziladi (`^` boshqa amal).

## 6. Kvadrat hisoblash

**Masala.** Shunday dastur yozing: butun va kasr sonlarning kvadratini funksiya yordamida hisoblaydi.

Namuna:

```text
Butun son: 7
Kasr son: 2.5
Butun 7 son kvadrati = 49
Kasr 2.5 son kvadrati = 6.25
```

??? success "Yechim"

    ```python
    def kvadrat(x):
        return x ** 2

    def main():

        iraqam = int(input("Butun son: "))
        fraqam = float(input("Kasr son: "))

        print(f"Butun {iraqam} son kvadrati = {kvadrat(iraqam)}")
        print(f"Kasr {fraqam} son kvadrati = {kvadrat(fraqam)}")

    main()
    ```

    Fayl: [p6.py](../../../downloads/dasturlash/week-02/p6.py)

    **Tushuntirish.**

    - `return` — funksiyadan **natijani qaytaradi**. Bu `print` dan farq qiladi: `print` qiymatni ekranga chiqaradi, `return` esa qiymatni chaqirgan joyga beradi va uni o'zgaruvchiga saqlash yoki boshqa ifodada ishlatish mumkin.
    - `return x ** 2` bajarilganda funksiya **darhol tugaydi** va `x ** 2` ning qiymati chaqirilgan joyga "almashib" qo'yiladi. Ya'ni `kvadrat(7)` ifodasi `49` ga aylanadi, go'yo kodda `49` yozilgandek.
    - Shuning uchun qaytgan qiymatni to'g'ridan-to'g'ri ishlatish mumkin: `a = kvadrat(7)`, `kvadrat(3) + 1`, `print(kvadrat(2))`. `return` dan keyin yozilgan qatorlar bajarilmaydi.
    - Taqqoslang: agar funksiya ichida `return x ** 2` o'rniga `print(x ** 2)` yozilsa, son ekranda ko'rinadi, lekin f-string ichida `{kvadrat(iraqam)}` ishlatib bo'lmaydi (u `None` chiqaradi).
    - `kvadrat(iraqam)` ifodasi qiymatga aylanadi (`49`), shuning uchun uni f-string `{ }` ichiga to'g'ridan-to'g'ri yozish mumkin.
    - Bitta funksiya ham `int`, ham `float` bilan ishlaydi: `7 ** 2` → `49` (`int`), `2.5 ** 2` → `6.25` (`float`).
    - `int(input(...))` va `float(input(...))` — kiritilgan matnni mos songa aylantiradi. `int` ga `"2.5"` kiritsangiz, `ValueError` chiqadi.

## 7. Kichik harfga o'tkazish

**Masala.** Shunday dastur yozing: xabarni to'liq kichik harflarda chiqaradi.

Namuna:

```text
Nma? SaLoM DuNyo
salom dunyo
```

??? success "Yechim"

    ```python
    habar = input("Nma? ")

    habar = habar.lower()
    print(habar)
    ```

    Fayl: [p7.py](../../../downloads/dasturlash/week-02/p7.py)

    **Tushuntirish.**

    - `.lower()` — satrdagi barcha harflarni kichik harfga o'tkazadi. Teskarisi — `.upper()`.
    - `.title()` bilan farqi: `title()` har so'zni bosh harfdan boshlaydi, `lower()` hamma harfni kichik qiladi.
    - `input("Nma? ")` da savol oxiridagi probel muhim: u foydalanuvchi yozgan matnni savoldan ajratib turadi. Probel bo'lmasa, matn savolga yopishib qoladi (`Nma?salom`).
    - Natija qayta `habar` ga saqlanadi, chunki `lower()` yangi satr qaytaradi.

## 8. Bo'sh joylarni almashtirish

**Masala.** Shunday dastur yozing: xabardagi har bir bo'sh joyni `...` bilan almashtiradi.

Namuna:

```text
Nma? Men Python o'rganyapman
Men...Python...o'rganyapman
```

??? success "Yechim"

    ```python
    habar = input("Nma? ")

    habar = habar.replace(" ", "...")

    print(habar)
    ```

    Fayl: [p8.py](../../../downloads/dasturlash/week-02/p8.py)

    **Tushuntirish.**

    - `satr.replace(eski, yangi)` — satrdagi `eski` qismning **hamma** uchragan joyini `yangi` bilan almashtiradi.
    - Almashtiriladigan va yangi qism bir belgi bo'lishi shart emas: bu yerda bitta bo'sh joy uchta nuqtaga almashdi.
    - Agar `eski` qism topilmasa, satr o'zgarishsiz qaytadi.
    - `replace` katta-kichik harfni farqlaydi: `"a"` ni almashtirsangiz, `"A"` o'zgarmaydi.

## 9. Emoji'larga almashtirish

**Masala.** Shunday dastur yozing: matndagi `:)` va `:(` belgilarini emoji'ga o'zgartiradi.

Namuna:

```text
Nma gap? Zo'r :) lekin charchadim :(
Zo'r 😊 lekin charchadim 😒
```

??? success "Yechim"

    ```python
    habar = input("Nma gap? ")

    habar = habar.replace(":)", "😊")
    habar = habar.replace(":(", "😒")

    print(habar)
    ```

    Fayl: [p9.py](../../../downloads/dasturlash/week-02/p9.py)

    **Tushuntirish.**

    - Ikkita `replace()` ketma-ket qo'llanadi: birinchisi `:)` ni, ikkinchisi `:(` ni almashtiradi. Har biri oldingisining natijasi ustida ishlaydi.
    - Emoji ham oddiy Unicode belgi, shuning uchun uni satr ichiga yozish mumkin (1-haftada ko'rgan `ord("😊")` ni eslang).
    - Ba'zi terminallar emoji'ni ko'rsata olmasligi mumkin. Bunda dasturda xato yo'q, muammo terminalning shriftida yoki kodlashida bo'ladi.

## 10. Massadan energiyani hisoblash

**Masala.** Shunday dastur yozing: berilgan massaga mos energiyani Eynshteyn formulasi `E = m · c²` bo'yicha hisoblaydi (`c` — yorug'lik tezligi, taxminan 300 000 000 m/s).

Namuna:

```text
Massa: 2
E = 180000000000000000
```

??? success "Yechim"

    ```python
    c = 300_000_000

    m = float(input("Massa: "))

    e = round(m * c ** 2)

    print(f"E = {e}")
    ```

    Fayl: [p10.py](../../../downloads/dasturlash/week-02/p10.py)

    **Tushuntirish.**

    - `300_000_000` — Python raqamlar orasida `_` belgisini qabul qiladi; u faqat o'qishni osonlashtiradi, qiymatga ta'sir qilmaydi. Bu aynan `300000000` bilan bir xil.
    - `c` — qiymati o'zgarmaydigan **doimiy** (konstanta) sifatida ishlatilgan. Python buni majburlamaydi, lekin odatda bunday qiymatlarga qayta qiymat berilmaydi.
    - `float(input(...))` — massa kasr son bo'lishi mumkin (`0.5`).
    - `m * c ** 2` — formuladagi `m · c²`. `**` ustuvorligi `*` dan yuqori, shuning uchun avval `c ** 2` hisoblanadi, keyin `m` ga ko'paytiriladi. Qavs shart emas.
    - `round(x)` — sonni eng yaqin butun songa yaxlitlaydi (`round(2.7)` → `3`); `.5` holatida juft songa qarab yaxlitlaydi. `round(x, 2)` ikkinchi argument bilan kasr raqamlari sonini beradi.
    - `float` ni `round` qilgach, natija `int` bo'ladi, shuning uchun natija `1.8e+17` ko'rinishida emas, kasrsiz yoziladi.

## 11. Choy puli (tip) hisoblash

**Masala.** Shunday dastur yozing: hisob summasi (`$` belgisi bilan) va foizni (`%` belgisi bilan) oladi va choy pulini hisoblaydi.

Namuna:

```text
Qancha boldi? $50
Nechi foiz? 15%
Tip: 7.50
```

??? success "Yechim"

    ```python
    def main():
        narh = narh_to(input("Qancha boldi? "))
        foiz = foiz_to(input("Nechi foiz? "))

        tip = narh * foiz

        print(f"Tip: {tip:.2f}")



    def narh_to(n):

        n = n.strip("$")

        return float(n)

    def foiz_to(f):

        f = f.strip("%")

        return float(f) / 100


    main()
    ```

    Fayl: [p11.py](../../../downloads/dasturlash/week-02/p11.py)

    **Tushuntirish.**

    - Dastur uch qismga bo'lingan: `main()` — asosiy oqim, `narh_to()` — summani songa aylantirish, `foiz_to()` — foizni songa aylantirish. Har funksiya bitta ishni bajaradi.
    - **Bu yerda `return` nega kerak.** `narh_to()` va `foiz_to()` hech narsa chiqarmaydi: ular hisoblangan sonni `return` bilan `main()` ga **qaytaradi**. `narh = narh_to(input(...))` qatorida `narh_to(...)` ifodasi qaytgan songa (`50.0`) almashadi va u `narh` ga saqlanadi. Keyin `narh * foiz` kabi hisoblarda ishlatiladi. Agar `return` bo'lmasa, `narh` ichida `None` bo'lardi va `narh * foiz` xato berardi (`TypeError`).
    - Ma'lumot oqimi: `main` → argument → funksiya → `return` → `main`. Funksiya tashqi dunyodan **parametr** orqali oladi va **return** orqali beradi; `n` va `f` o'zgaruvchilari esa faqat o'z funksiyasi ichida mavjud.
    - `n.strip("$")` — `strip` ga argument berilsa, satrning **boshi va oxiridan** shu belgilarni olib tashlaydi: `"$50"` → `"50"`. Belgi bo'lmasa, satr o'zgarmaydi, shuning uchun `50` kiritilsa ham dastur ishlaydi.
    - `float("50")` → `50.0`. Matn faqat son shaklida bo'lgandagina `float()` ishlaydi; `"$50"` ni to'g'ridan-to'g'ri aylantirsak, `ValueError` chiqardi.
    - `float(f) / 100` — foizni ulushga aylantiradi: `15` → `0.15`.
    - `tip = narh * foiz` → `50.0 * 0.15` = `7.5`.
    - `{tip:.2f}` — f-string formatlash: `.2f` natijani **ikki kasr raqami** bilan chiqaradi (`7.5` → `7.50`).
    - Funksiyalar `main()` dan keyin yozilgan, lekin `main()` eng oxirida chaqirilgani uchun muammo yo'q: Python chaqiruv paytiga kelib hamma funksiyani biladi.

## Qisqa lug'at

| Tushuncha | Ma'nosi |
|---|---|
| `input(savol)` | savolni chiqarib, foydalanuvchi matnini qaytaradi |
| `satr.strip()`, `satr.strip(belgilar)` | boshi va oxiridagi bo'sh joylarni (yoki ko'rsatilgan belgilarni) olib tashlaydi |
| `satr.title()` / `lower()` / `upper()` | har so'zni bosh harfli / hammasini kichik / hammasini katta qiladi |
| `satr.split()` | bo'sh joylar bo'yicha bo'lib, ro'yxat qaytaradi |
| `satr.replace(eski, yangi)` | barcha `eski` qismlarni `yangi` ga almashtiradi |
| `int()`, `float()` | matnni butun / o'nlik songa aylantiradi |
| `round(x)` | eng yaqin butun songa yaxlitlaydi |
| `def nom(parametr):` | funksiya yaratadi; `return` natija qaytaradi |
| `f"{qiymat:.2f}"` | qiymatni ikki kasr raqami bilan chiqaradi |
