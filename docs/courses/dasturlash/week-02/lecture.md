# 2-hafta. Python dasturlashga kirish

Ma'ruza taqdimoti: [Python dasturlashga kirish (PPTX)](../../../downloads/dasturlash/week-02/python-dasturlash-kirish.pptx)

Bu haftaning amaliy qismi: [amaliyot](practice.md).

## Python dasturi qanday ishlaydi

Kompyuterning asosiy qismlari: **protsessor (CPU)** buyruqlarni bajaradi, **xotira (RAM)** dastur ishlayotganda ma'lumotni vaqtincha saqlaydi, **qattiq disk / SSD** fayllarni doimiy saqlaydi. Klaviatura va sichqoncha kiritish qurilmalari, monitor esa chiqarish qurilmasi hisoblanadi.

Biz yozgan matn **manba kod** (*source code*) deyiladi. Protsessor uni to'g'ridan-to'g'ri tushunmaydi: u faqat nollar va birlarni (mashina kodini) bajaradi. Kodni bajarish vazifasini **interpreter** bajaradi. Python avval butun faylni tekshirib, uni **bayt-kod** (*bytecode*) deb ataladigan oraliq ko'rinishga o'giradi, so'ng interpreter bu buyruqlarni birma-bir bajaradi. Shuning uchun faylning istalgan joyida sintaksis xatosi bo'lsa, dastur umuman ishga tushmaydi — hatto xatodan oldingi qatorlar ham bajarilmaydi. `python hello.py` buyrug'i ikkala bosqichni birga bajaradi, shuning uchun biz "yozdik, ishga tushirdik, natijani ko'rdik" tarzida ishlay olamiz.

```text
manba kod (.py)  →  bayt-kod  →  interpreter buyruqlarni birma-bir bajaradi
```

Dastur `.py` kengaytmali faylda saqlanadi. Terminalda uni quyidagicha ishga tushiramiz:

```bash
python hello.py
```

!!! note "Windows'da"
    Agar `python` buyrug'i ishlamasa, `py hello.py` ni sinab ko'ring.

## Birinchi dastur: `print()`

`print()` — Python'ning tayyor (*built-in*) **funksiyasi**. Funksiya — kompyuter oldindan bajarishni biladigan harakat ("fe'l"). Qavs ichiga yozilgan qiymat funksiyaning **argumenti** deyiladi.

```python
print("Salom, dunyo!")
```

```text
Salom, dunyo!
```

Matn **qo'shtirnoq** (`"`) yoki yakka tirnoq (`'`) ichida yozilishi shart. Matn **satr** (*string*) deb ataladi. Tirnoqsiz yozsak, Python buni buyruq yoki nom deb o'ylaydi va xato beradi.

Dastur buyruqlarni **yuqoridan pastga, birma-bir** bajaradi:

```python
print("Dasturlashga xush kelibsiz!")
print("Avval print buyrug'ini mashq qilamiz.")
print("Bu dastur ekranga uch qator matn chiqaradi.")
```

```text
Dasturlashga xush kelibsiz!
Avval print buyrug'ini mashq qilamiz.
Bu dastur ekranga uch qator matn chiqaradi.
```

### Hisoblash va matnni farqlash

Tirnoqsiz yozilgan ifodani Python **hisoblaydi**, tirnoq ichidagini esa **matn sifatida** chiqaradi:

```python
print(2 + 2 * 10)
print("2 + 2 * 10")
```

```text
22
2 + 2 * 10
```

### Izohlar

`#` belgisidan keyingi matnni Python e'tiborsiz qoldiradi. Izoh kodni o'qiydigan odamga tushuntirish beradi:

```python
print("Bir yilda soat:")
# yilda 365 kun, har kunda 24 soat
print(365 * 24)  # qator oxirida ham izoh yozish mumkin
```

```text
Bir yilda soat:
8760
```

Izohda *nima qilinayotganini* emas, *nima uchun* shunday qilinayotganini yozing. Murakkab masalani yechishdan oldin izohlarda **psevdokod** yozib, keyin har qatorni haqiqiy kodga aylantirish ham yaxshi odat.

## Xatolar (bug)

Xato (*bug*) — dasturlashning tabiiy qismi. Python xatoni topsa, xabar chiqaradi va qaysi qatorda ekanini ko'rsatadi:

```python
print("Salom)
```

```text
  File "hello.py", line 1
    print("Salom)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

Xabarni pastdan yuqoriga o'qing: oxirgi qatorda xato turi va tavsifi, uning ustida esa fayl nomi, qator raqami (`line 1`) va xato joyini ko'rsatuvchi `^` belgisi. Bu yerda tirnoq yopilmagan. Xato xabarini o'qish — dasturchining asosiy ko'nikmasi.

## Foydalanuvchidan ma'lumot: `input()` va o'zgaruvchilar

`input()` foydalanuvchi klaviaturada yozgan matnni qabul qiladi. Olingan qiymatni saqlash uchun **o'zgaruvchi** kerak. O'zgaruvchi — nomi bor "quti" bo'lib, ichida qiymat saqlanadi.

```python
ism = input("Ismingiz nima? ")
print("Salom,", ism)
```

```text
Ismingiz nima? Laylo
Salom, Laylo
```

`=` belgisi matematikadagi "teng" emas, **o'zlashtirish** (*assignment*) operatoridir: o'ngdagi qiymat chapdagi nomga saqlanadi.

!!! warning "Muhim"
    `input()` har doim natijani **matn (`str`)** sifatida qaytaradi, hatto foydalanuvchi son yozgan bo'lsa ham.

### Bir nechta o'zgaruvchi

```python
ism = input("Ismingiz: ")
email = input("Elektron pochtangiz: ")
laqab = input("Laqabingiz: ")

print("Ism:", ism)
print("Pochta:", email)
print("Laqab:", laqab)
```

### Qiymatni o'zgartirish

O'zgaruvchining yangi qiymati eskisini **almashtiradi**; eski qiymat yo'qoladi. Yangi qiymat eskisiga asoslanishi ham mumkin:

```python
soz = "salom"
print(soz)
soz = "xayr"
print(soz)
soz = soz + "!!!"
print(soz)
```

```text
salom
xayr
xayr!!!
```

### O'zgaruvchi nomlari

- Nom harf yoki `_` bilan boshlanadi; faqat harf, raqam va `_` bo'lishi mumkin;
- katta-kichik harf farqlanadi: `ism`, `Ism` va `ISM` — uch xil nom;
- bo'sh joy bo'lmaydi; so'zlar `_` bilan ajratiladi: `tugilgan_yil` (`snake_case`);
- nom mazmunni bildirsin: `a` emas, `yosh`;
- `if`, `else`, `def` kabi **kalit so'zlarni** nom qilib bo'lmaydi: `if = 5` — `SyntaxError`;
- `print`, `input` kabi tayyor funksiya nomlarini ham ishlatmang: `print = 5` xato bermaydi, lekin shundan keyin `print()` funksiyasi ishlamay qoladi.

Dasturlash tillarining kalit so'zlari ingliz tilida, shuning uchun o'zgaruvchi nomlarini ham ingliz tilida yozish xalqaro odat. Bu kursda tushunarli bo'lishi uchun ba'zan o'zbekcha nomlar ham uchraydi; muhimi — nom izchil va mazmunli bo'lishi.

## Ma'lumot turlari

Har bir qiymatning **turi** (*type*) bor. Tur qiymat bilan qanday amal bajarish mumkinligini belgilaydi.

| Tur | Nomi | Misol |
|---|---|---|
| `int` | butun son | `-15`, `0`, `42` |
| `float` | kasr son | `2.5`, `-1.25`, `3.62` |
| `str` | satr (matn) | `"salom"`, `"100"` |

Katta sonlarni o'qishni osonlashtirish uchun raqamlar orasiga `_` qo'yish mumkin: `300_000_000` — aynan `300000000` ning o'zi.

Turni `type()` funksiyasi ko'rsatadi:

```python
print(type(100))
print(type(2.5))
print(type("100"))
```

```text
<class 'int'>
<class 'float'>
<class 'str'>
```

`100` va `"100"` — **har xil** qiymatlar. `+` operatori sonlarda qo'shadi, satrlarda esa ularni **ulaydi** (*concatenation*):

```python
son = 100
matn = "100"
print(son + son)
print(matn + matn)
```

```text
200
100100
```

## Turlarni o'zgartirish

Satr va sonni `+` bilan qo'shib bo'lmaydi:

```python
yosh = 20
print("Yoshim: " + yosh)
```

```text
TypeError: can only concatenate str (not "int") to str
```

Yechim — turni o'zgartirish (*type casting*):

| Funksiya | Vazifasi | Misol |
|---|---|---|
| `int(x)` | butun songa o'tkazadi | `int("42")` → `42` |
| `float(x)` | kasr songa o'tkazadi | `float("2.5")` → `2.5` |
| `str(x)` | satrga o'tkazadi | `str(42)` → `"42"` |

`input()` dan son olish uchun uni darhol `int()` yoki `float()` ga o'raymiz:

```python
tugilgan_yil = int(input("Qaysi yilda tug'ilgansiz? "))
print("Siz 2026-yilda", 2026 - tugilgan_yil, "yoshga to'lasiz")
```

```text
Qaysi yilda tug'ilgansiz? 2008
Siz 2026-yilda 18 yoshga to'lasiz
```

`int("salom")` kabi songa aylanmaydigan matn `ValueError` beradi. Hozircha foydalanuvchi to'g'ri qiymat kiritadi deb hisoblaymiz.

## Qiymatlarni birga chiqarish

Aralash ma'lumotni chiqarishning uch usuli bor.

**1. Vergul bilan.** `print()` qiymatlar orasiga o'zi bo'sh joy qo'yadi, turlarni o'zgartirish shart emas:

```python
natija = 10 * 25
print("Natija:", natija)
```

**2. `str()` va `+` bilan.** Bo'sh joyni o'zingiz yozasiz:

```python
print("Natija: " + str(natija))
```

**3. f-string** — eng qulay usul. Satr oldiga `f` qo'yiladi, o'zgaruvchilar `{ }` ichiga yoziladi:

```python
ism = "Mark"
yosh = 37
shahar = "Toshkent"
print(f"Salom, {ism}! Siz {yosh} yoshdasiz va {shahar}da yashaysiz.")
```

```text
Salom, Mark! Siz 37 yoshdasiz va Toshkentda yashaysiz.
```

f-string'da `{ }` ichiga ifoda ham yozish mumkin: `print(f"{2 + 3}")` → `5`. Matnning qaysi qismida bo'sh joy bo'lishini siz aniq nazorat qilasiz, shuning uchun biz asosan shu usulni ishlatamiz.

## Satrlar bilan ishlash

Satrning tayyor **metodlari** bor. Metod `satr.metod()` ko'rinishida chaqiriladi:

```python
ism = input("Ismingiz: ")
ism = ism.strip().title()
print(f"Salom, {ism}")
```

```text
Ismingiz:   laylo karimova  
Salom, Laylo Karimova
```

- `.strip()` — boshi va oxiridagi bo'sh joylarni olib tashlaydi;
- `.title()` — har bir so'zni bosh harf bilan boshlaydi;
- `.upper()`, `.lower()` — hammasini katta yoki kichik harfga o'tkazadi.

Metodlarni ketma-ket **zanjirlash** mumkin: `ism.strip().title()`.

!!! warning "O'zbekcha ismlar va `.title()`"
    `.title()` tutuq belgisi (`'`) dan keyingi harfni ham yangi so'z boshi deb hisoblaydi: `"o'tkir g'ulomov".title()` → `"O'Tkir G'Ulomov"`. O'zbekcha matnda uning o'rniga `string.capwords()` ishlating. U matnni bo'sh joylar bo'yicha so'zlarga ajratadi va har bir so'zning faqat birinchi harfini katta qiladi:

    ```python
    import string

    ism = string.capwords("o'tkir g'ulomov")
    print(ism)
    ```

    ```text
    O'tkir G'ulomov
    ```

    `import string` — Python bilan birga keladigan `string` modulini ulaydi; modullarni keyinroq batafsil o'rganamiz. Bitta so'z uchun `.capitalize()` yetarli: `"o'tkir".capitalize()` → `"O'tkir"`.

Yana uchta foydali metod (ular [amaliyotda](practice.md) ishlatiladi):

- `.replace(eski, yangi)` — satrdagi barcha `eski` qismlarni `yangi` bilan almashtiradi: `"a b c".replace(" ", "...")` → `"a...b...c"`;
- `.split()` — satrni bo'sh joylar bo'yicha bo'laklarga ajratadi va **ro'yxat** qaytaradi: `"ali valiyev".split()` → `["ali", "valiyev"]`. Bo'laklarni darhol alohida o'zgaruvchilarga ochish mumkin: `ism, familiya = "ali valiyev".split()`. Bo'laklar soni o'zgaruvchilar soniga teng bo'lishi shart, aks holda `ValueError`;
- `.strip(belgilar)` — argument berilsa, bo'sh joy o'rniga shu belgilarni boshi va oxiridan olib tashlaydi: `"$50".strip("$")` → `"50"`.

Qo'shtirnoq ichida qo'shtirnoq kerak bo'lsa, tashqarisida yakka tirnoq ishlating: `print('U "salom" dedi')`. Yoki `\"` yozing: teskari chiziq (`\`) keyingi belgini oddiy belgiga aylantiradi. Qatorni almashtirmasdan chiqarish uchun: `print("Salom,", end="")`.

## Arifmetik amallar

| Amal | Nomi | Misol | Natija |
|:---:|---|---|---|
| `+` | qo'shish | `2 + 4` | `6` |
| `-` | ayirish | `10 - 2.5` | `7.5` |
| `*` | ko'paytirish | `-2 * 123` | `-246` |
| `/` | bo'lish (har doim `float`) | `9 / 2` | `4.5` |
| `//` | butun bo'lish (pastga yaxlitlaydi) | `9 // 2` | `4` |
| `%` | qoldiq (modul) | `9 % 2` | `1` |
| `**` | darajaga ko'tarish | `2 ** 3` | `8` |

```python
print(9 / 2)
print(9 // 2)
print(9 % 2)
print(8 / 2)
```

```text
4.5
4
1
4.0
```

E'tibor bering: `8 / 2` natijasi `4.0` — `/` har doim `float` qaytaradi. Ikki `int` ustida `+ - * // % **` natijasi `int` (faqat `**` da daraja manfiy bo'lsa, `float`: `2 ** -1` → `0.5`), agar bitta operand `float` bo'lsa, natija `float` bo'ladi.

`%` va `//` bir-biriga bog'liq: `a == (a // b) * b + a % b`. Masalan, `175` soniyani daqiqaga aylantirish: `175 // 60` = `2` daqiqa, `175 % 60` = `55` soniya. Juft-toqni aniqlashda ham `%` ishlatiladi: `n % 2` juft sonda `0`, toq sonda `1` beradi.

### Amallar ustuvorligi

Avval `**`, keyin `*`, `/`, `//`, `%`, oxirida `+`, `-`. Qavs tartibni o'zgartiradi:

```python
print(2 + 2 * 10)
print((2 + 2) * 10)
print(2 ** 3 * 2)
print(2 ** (3 * 2))
```

```text
22
40
16
64
```

### Amallarni o'zgaruvchilar bilan

```python
tomon = float(input("Kvadrat tomoni (sm): "))
yuza = tomon ** 2
perimetr = 4 * tomon
print(f"Yuza: {yuza}, perimetr: {perimetr}")
```

```text
Kvadrat tomoni (sm): 2.5
Yuza: 6.25, perimetr: 10.0
```

### Yig'indi to'plash

O'zgaruvchini o'zining eski qiymati asosida o'zgartirish juda ko'p uchraydi. Buning qisqa yozuvi bor:

```python
jami = 0
jami = jami + 5
jami += 3     # jami = jami + 3 bilan bir xil
jami *= 2     # jami = jami * 2
print(jami)
```

```text
16
```

Shu kabi `-=`, `/=`, `//=`, `%=`, `**=` ham bor.

## Natijani chiroyli chiqarish

Kasr sonlarda ba'zan ortiqcha raqamlar chiqadi: `1 / 3` → `0.3333333333333333`. f-string'da `:` dan keyin format yoziladi:

```python
x = 1 / 3
print(f"{x:.2f}")       # 2 ta kasr raqami
print(f"{1234567:,}")   # mingliklarni vergul bilan ajratish
print(f"{1234567.891:,.2f}")
print(round(2.675, 2), round(7.5), round(8.5))
```

```text
0.33
1,234,567
1,234,567.89
2.67 8 8
```

`round(x)` eng yaqin butun songa yaxlitlaydi; `x.5` holatida **juft** songa qarab yaxlitlaydi (`7.5` → `8`, `8.5` → `8`). `round(2.675, 2)` esa `2.67` beradi, chunki `2.675` kompyuterda aniq saqlanmaydi (kasr sonlar ikkilik tizimda taxminan ifodalanadi). `:.2f` ham faqat ko'rinishni o'zgartiradi va xuddi shu cheklovga ega: `f"{2.675:.2f}"` ham `2.67` beradi. Natijani chiqarishda `:.2f` qulay, lekin pul hisob-kitobida bu farq muhim bo'lishi mumkin; aniq hisob usullarini keyinroq o'rganamiz.

## To'liq misol: tana vazn indeksi (BMI)

```python
bo_y = float(input("Bo'yingiz (sm): "))
vazn = float(input("Vazningiz (kg): "))

bo_y = bo_y / 100          # santimetrni metrga o'tkazamiz
bmi = vazn / bo_y ** 2
print(f"BMI: {bmi:.1f}")
```

```text
Bo'yingiz (sm): 180
Vazningiz (kg): 75
BMI: 23.1
```

Tahlil: kirish — ikki `float`; formula `vazn / bo'y²`; `**` ustuvorligi sababli `bo_y ** 2` avval hisoblanadi, keyin bo'linadi; natija bir kasr raqamigacha chiqariladi.

## Odatiy xatolar

- **Matn bilan sonni `+` bilan ulash.** `"Yosh: " + 20` → `TypeError`. `str(20)` yoki f-string ishlating.
- **`input()` natijasini son deb o'ylash.** `input("a: ") + input("b: ")` `3` va `4` uchun `34` beradi, `7` emas. `int()` ga o'rang.
- **Tirnoqni yopishni unutish** yoki ichma-ich bir xil tirnoq ishlatish.
- **`=` va "teng" ni adashtirish.** `5 = x` xato: chapda nom turishi kerak.
- **`/` natijasini `int` deb kutish.** `10 / 2` → `5.0`. Butun natija kerak bo'lsa, `//`.
- **Ustuvorlikni unutish.** `2 + 3 * 4` — `20` emas, `14`. Shubha bo'lsa, qavs ishlating.
- **Nomda xato.** `Ism` va `ism` bir xil emas; yozilmagan nom `NameError` beradi.
- **`print` dan keyin qavsni unutish.** `print "salom"` Python 3'da ishlamaydi.
- **O'zbekcha ismga `.title()` ishlatish.** `"g'ayrat".title()` → `"G'Ayrat"`. `string.capwords()` yoki bitta so'z uchun `.capitalize()` ishlating.
