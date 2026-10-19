# 3-hafta. Funksiyalar, shartlar, scope va turlar

Ma'ruza taqdimoti: [Funksiyalar, shartlar, scope va turlar (PPTX)](../../../downloads/dasturlash/week-03/funksiyalar-shartlar-scope-turlar.pptx)

Bu haftaning amaliy qismi: [amaliyot](practice.md).

## Funksiyalar

Funksiya — nomi bor, qayta ishlatish mumkin bo'lgan kod bo'lagi. Siz `print()`, `input()`, `int()`, `round()` kabi tayyor funksiyalarni allaqachon ishlatgansiz. Endi o'zimizning funksiyamizni yaratamiz.

Taksi narxi 5 000 so'm + har kilometr uchun 2 000 so'm bo'lsin. Funksiyasiz hisob takrorlanadi:

```python
narx1 = 5000 + 3 * 2000
narx2 = 5000 + 7 * 2000
narx3 = 5000 + 12 * 2000
```

Tarif o'zgarsa, uch joyni tuzatish kerak; yuz joyda ishlatilgan bo'lsa-chi? Formulani funksiyaga ajratamiz:

```python
def taksi_narxi(km):
    return 5000 + km * 2000


print(taksi_narxi(3))
print(taksi_narxi(7))
print(taksi_narxi(12))
```

```text
11000
19000
29000
```

- `def` — yangi funksiya yaratadi. `taksi_narxi` — funksiya nomi.
- `km` — **parametr**: funksiya chaqirilganda unga tushadigan qiymat uchun nom.
- `taksi_narxi(3)` da `3` — **argument**: parametrga beriladigan haqiqiy qiymat.
- Funksiya tanasi **4 ta probel chekinish** bilan yoziladi.
- `return` natijani funksiyadan chaqirilgan joyga **qaytaradi** va funksiyani tugatadi. `taksi_narxi(3)` ifodasi `11000` ga aylanadi.

`def` funksiyani faqat **yaratadi**, ishga tushirmaydi. U chaqirilganda ishlaydi.

Funksiyaning uch afzalligi: kod **takrorlanmaydi**, **oson o'zgaradi** (tuzatish bitta joyda), **oson o'qiladi** (nom nima qilishini aytadi).

### Parametr va standart qiymat

Parametrga **standart qiymat** berish mumkin. Argument berilmasa, shu qiymat ishlatiladi:

```python
def hello(to="Jigarlar"):
    print("Salom,", to)


hello("Aziz")
hello()
```

```text
Salom, Aziz
Salom, Jigarlar
```

### `main()` funksiyasi

Dasturning asosiy qismini `main()` ga yig'ish va eng oxirida chaqirish odat:

```python
def main():
    ism = input("Ismingiz? ")
    hello(ism)


def hello(to="Jigarlar"):
    print("Salom,", to)


main()
```

`hello` `main` dan keyin yozilgan, lekin muammo yo'q: `main()` eng oxirida chaqiriladi, shu paytga kelib ikkala funksiya ham yaratilgan bo'ladi.

### `return`: natijani qaytarish

`print` qiymatni ekranga chiqaradi, `return` esa uni funksiyadan **chaqirgan joyga beradi**. Qaytgan qiymatni o'zgaruvchiga saqlash yoki boshqa ifodada ishlatish mumkin:

```python
def main():
    x = int(input("x ni kiriting: "))
    print("x ning kvadrati:", kvadrat(x))


def kvadrat(n):
    return n * n


main()
```

```text
x ni kiriting: 5
x ning kvadrati: 25
```

`return` bo'lmagan funksiya `None` qaytaradi. `None` — "hech qanday qiymat yo'q" degan maxsus qiymat.

## Shartlar

Dasturlar ba'zan qaror qabul qilishi kerak: shart bajarilsa bir ish, bajarilmasa boshqa ish. Buning uchun **shartli operatorlar** ishlatiladi.

### Taqqoslash operatorlari

Taqqoslash natijasi **mantiqiy qiymat** — `True` (to'g'ri) yoki `False` (noto'g'ri) bo'ladi. Bundan keyin bu qiymatlarni Python'dagidek `True` va `False` deb yozamiz.

| Operator | Ma'nosi | Misol | Natija |
|:---:|---|---|:---:|
| `>` | katta | `5 > 3` | `True` |
| `<` | kichik | `5 < 3` | `False` |
| `>=` | katta yoki teng | `5 >= 5` | `True` |
| `<=` | kichik yoki teng | `4 <= 3` | `False` |
| `==` | teng | `10 == 7` | `False` |
| `!=` | teng emas | `10 != 7` | `True` |

`=` va `==` ni adashtirmang: `x = 5` — `x` ga `5` ni **beradi**; `x == 5` — `x` `5` ga tengligini **tekshiradi**.

### `if`

```python
x = int(input("x ni kiriting: "))
y = int(input("y ni kiriting: "))

if x < y:
    print("x y dan kichik")
```

`if` dan keyin shart yoziladi, so'ng `:` qo'yiladi. Shart `True` bo'lsa, **chekinish bilan** yozilgan qatorlar bajariladi, aks holda o'tkazib yuboriladi.

```text
x ni kiriting: 1
y ni kiriting: 2
x y dan kichik
```

`x = 3`, `y = 2` kiritilsa, hech narsa chiqmaydi.

### `elif` va `else`

Uch holatni (`<`, `>`, `==`) alohida `if` bilan tekshirish mumkin:

```python
if x < y:
    print("x y dan kichik")
if x > y:
    print("x y dan katta")
if x == y:
    print("x y ga teng")
```

Bu ishlaydi, lekin samarasiz: `x < y` `True` bo'lsa ham, qolgan ikki shart baribir tekshiriladi. `elif` ("else if") oldingi shart bajarilmagandagina keyingisini tekshiradi:

```python
if x < y:
    print("x y dan kichik")
elif x > y:
    print("x y dan katta")
elif x == y:
    print("x y ga teng")
```

Uchta holatdan biri albatta bo'lgani uchun oxirgi shartni `else` bilan almashtirish mumkin. `else` yuqoridagi hech bir shart bajarilmaganda ishlaydi:

```python
x = int(input("x ni kiriting: "))
y = int(input("y ni kiriting: "))

if x < y:
    print("x y dan kichik")
elif x > y:
    print("x y dan katta")
else:
    print("x y ga teng")
```

```text
x ni kiriting: 4
y ni kiriting: 4
x y ga teng
```

Qoida: shartlar **yuqoridan pastga** tekshiriladi va sharti `True` bo'lgan **birinchi** blok bajariladi, qolganlari o'tkazib yuboriladi. Tuzilma: bitta `if`, istalgancha `elif`, ixtiyoriy bitta `else`.

### `or`: "yoki"

`or` bilan bog'langan shartlardan **kamida bittasi** `True` bo'lsa, butun shart `True`:

```python
if x < y or x > y:
    print("x y ga teng emas")
else:
    print("x y ga teng")
```

Xuddi shu ishni `!=` operatori qisqaroq bajaradi:

```python
if x != y:
    print("x y ga teng emas")
else:
    print("x y ga teng")
```

### `and`: "va"

`and` bilan bog'langan **hamma** shartlar `True` bo'lsagina butun shart `True`. Baholash misoli:

```python
ball = int(input("Ball: "))

if ball >= 90 and ball <= 100:
    print("Baho: A")
elif ball >= 80 and ball < 90:
    print("Baho: B")
elif ball >= 70 and ball < 80:
    print("Baho: C")
elif ball >= 60 and ball < 70:
    print("Baho: D")
else:
    print("Baho: F")
```

Python'da oraliqni matematikadagidek yozish mumkin:

```python
if 90 <= ball <= 100:
    print("Baho: A")
elif 80 <= ball < 90:
    print("Baho: B")
elif 70 <= ball < 80:
    print("Baho: C")
elif 60 <= ball < 70:
    print("Baho: D")
else:
    print("Baho: F")
```

Shartlar yuqoridan pastga tekshirilishi sababli kodni yana soddalashtirish mumkin: dastur `elif ball >= 80` gacha yetib kelgan bo'lsa, `ball >= 90` sharti `False` chiqqan, ya'ni ball 90 dan kichik. Shuning uchun yuqori chegarani yozish shart emas:

```python
ball = int(input("Ball: "))

if ball >= 90:
    print("Baho: A")
elif ball >= 80:
    print("Baho: B")
elif ball >= 70:
    print("Baho: C")
elif ball >= 60:
    print("Baho: D")
else:
    print("Baho: F")
```

```text
Ball: 85
Baho: B
```

Chegaraviy qiymatlarni tekshiring: `90` → A, `89` → B, `60` → D, `59` → F.

Bu soddalashtirish ball 0–100 oralig'ida kiritiladi deb hisoblaydi. Oraliqdan tashqaridagi ball uchun variantlar har xil ishlaydi: `150` birinchi variantda F, soddalashtirilganida A oladi. Noto'g'ri ballni alohida ushlash uchun boshiga yana bitta shart qo'shing:

```python
if ball < 0 or ball > 100:
    print("Ball 0 dan 100 gacha bo'lishi kerak")
elif ball >= 90:
    print("Baho: A")
...
```

Uchta mantiqiy operator bor: `and` ("va"), `or` ("yoki"), `not` ("emas"). `not` shartni teskarisiga o'giradi: `not (x == y)` — `x != y` bilan bir xil.

### Qoldiq operatori: juft yoki toq

`%` bo'lingandagi qoldiqni beradi: `4 % 2` → `0`, `3 % 2` → `1`, `7 % 3` → `1`. Son juft bo'lsa, 2 ga bo'lingandagi qoldiq `0` bo'ladi:

```python
x = int(input("x ni kiriting: "))

if x % 2 == 0:
    print("Juft")
else:
    print("Toq")
```

```text
x ni kiriting: 7
Toq
```

### Mantiqiy funksiyalar

Tekshiruvni funksiyaga ajratish mumkin. `True` yoki `False` qaytaradigan funksiyalar odatda `is_` bilan boshlanadi:

```python
def main():
    x = int(input("x ni kiriting: "))
    if is_even(x):
        print("Juft")
    else:
        print("Toq")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
```

Bu kodni qisqartirish mumkin. `if` o'rniga **shartli ifoda** ishlatamiz. U `A if shart else B` ko'rinishida yoziladi: shart `True` bo'lsa natija `A`, aks holda `B`:

```python
def is_even(n):
    return True if n % 2 == 0 else False
```

Aslida `n % 2 == 0` ifodasining o'zi `True` yoki `False` beradi, shuning uchun uni to'g'ridan-to'g'ri qaytarish yetarli. Bu eng "pythonic" (Python ruhiga mos) yozuv:

```python
def is_even(n):
    return n % 2 == 0
```

Uchala variant bir xil ishlaydi; oxirgisi eng qisqa va o'qishga qulay.

### `match`

Bitta o'zgaruvchining aniq qiymatlariga qarab tarmoqlanish kerak bo'lsa, uzun `elif` zanjiri o'rniga `match` ishlatish mumkin:

```python
kun = input("Hafta kuni? ")

match kun:
    case "shanba":
        print("Dam olish kuni")
    case "yakshanba":
        print("Dam olish kuni")
    case "dushanba":
        print("Haftaning boshi")
    case _:
        print("Ish kuni")
```

```text
Hafta kuni? yakshanba
Dam olish kuni
```

`case _` — hech bir variantga mos kelmaganda ishlaydi (`else` kabi). Bir xil natijali variantlarni `|` ("yoki") bilan birlashtirish mumkin:

```python
kun = input("Hafta kuni? ")

match kun:
    case "shanba" | "yakshanba":
        print("Dam olish kuni")
    case "dushanba":
        print("Haftaning boshi")
    case _:
        print("Ish kuni")
```

!!! note "Python versiyasi"
    `match` Python 3.10 dan boshlab mavjud. `python --version` bilan versiyangizni tekshiring.

## Scope: o'zgaruvchi qayerda ko'rinadi

**Scope** (ko'rinish sohasi) — o'zgaruvchi ko'rinadigan va ishlatilishi mumkin bo'lgan joy. Uni dars xonasidagi doskaga o'xshatish mumkin: doskadagi yozuvni faqat shu xonadagilar ko'radi, qo'shni xona uni ko'rmaydi.

### Local o'zgaruvchi

Funksiya ichida yaratilgan o'zgaruvchi **local** (mahalliy) deyiladi. U faqat o'sha funksiya ichida mavjud:

```python
def main():
    name = input("Ismingiz? ")
    hello()


def hello():
    print("Salom,", name)


main()
```

```text
Ismingiz? Anora
NameError: name 'name' is not defined
```

`name` — `main` ichidagi local o'zgaruvchi, `hello` uni ko'rmaydi. Yechim — qiymatni **argument** sifatida berish:

```python
def main():
    name = input("Ismingiz? ")
    hello(name)


def hello(to):
    print("Salom,", to)


main()
```

```text
Ismingiz? Anora
Salom, Anora
```

Dastur qadamma-qadam:

1. `main()` ishga tushadi: `name = "Anora"` — `name` `main` ichida local.
2. `hello(name)` — qiymat argument bo'lib `hello` ga o'tadi.
3. `to = "Anora"` — `to` `hello` ichida local.
4. `Salom, Anora` chiqadi; funksiya tugagach, `to` yo'qoladi.

Funksiya tugagach, uning ichidagi local o'zgaruvchilar yo'qoladi:

```python
def hisobla():
    natija = 5 * 2


hisobla()
print(natija)
```

```text
NameError: name 'natija' is not defined
```

### Global o'zgaruvchi

Fayl darajasida (hech qaysi funksiya ichida emas) yaratilgan o'zgaruvchi **global** deyiladi. Funksiya uni o'qiy oladi:

```python
kurs = "Dasturlash 1"   # global: fayl darajasida


def salom():
    print("Xush kelibsiz:", kurs)   # o'qish mumkin


salom()
```

```text
Xush kelibsiz: Dasturlash 1
```

Lekin funksiya ichida `=` yozilsa, global o'zgaruvchi o'zgarmaydi — shu nomli **yangi local** o'zgaruvchi yaratiladi:

```python
narx = 5000


def yangila():
    narx = 7000   # yangi, local narx


yangila()
print(narx)
```

```text
5000
```

To'g'ri yo'l — qiymatni funksiyaga argument bilan berish va yangisini `return` bilan qaytarish:

```python
narx = 5000


def yangila(narx):
    return narx + 2000


narx = yangila(narx)
print(narx)
```

```text
7000
```

### Scope qoidalari

1. **Local** — funksiya ichida yaratiladi, tashqarida ko'rinmaydi.
2. **Global** — fayl darajasida yaratiladi; funksiya uni o'qiy oladi.
3. **Kirish va chiqish** — qiymat funksiyaga argument bilan kiradi, `return` bilan chiqadi.

## Ma'lumot turlari

Har bir qiymatning turi bor: `5` va `"5"` bir xil emas, Python ular bilan har xil ishlaydi. [2-haftada](../week-02/lecture.md#malumot-turlari) `int`, `float`, `str` turlari va `type()` funksiyasi bilan tanishgansiz. Endi to'rtinchi asosiy tur — `bool` qo'shiladi:

| Tur | Nomi | Misol |
|---|---|---|
| `int` | butun son | `42`, `-7`, `0` |
| `float` | kasr son | `3.14`, `2.0` |
| `str` | satr (matn) | `"Salom"`, `"42"` |
| `bool` | mantiqiy qiymat | `True`, `False` |

```python
print(type(42))
print(type(3.14))
print(type("42"))
print(type(True))
```

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

`"42"` qo'shtirnoq ichida yozilgani uchun `str`, son emas.

### `int` va `float`

- `0` ham `int`; `1_000_000` — pastki chiziq faqat o'qishni osonlashtiradi.
- `2.0` butun ko'rinsa ham `float`, chunki nuqta bilan yozilgan.
- `1.5e6` — ilmiy yozuv: `1.5 · 10⁶`, ya'ni `1500000.0`.
- `3 + 2.0` → `5.0`: `int` va `float` aralashsa, natija `float`.

Kasr sonlar ikkilik tizimda taxminan saqlanadi, shuning uchun natijada kichik farq paydo bo'lishi mumkin:

```python
x = 0.1 + 0.2
print(x)
print(round(x, 2))
```

```text
0.30000000000000004
0.3
```

Natijani chiqarishda `round()` yoki `:.2f` ishlating.

### `str`

| Ifoda | Natija | Ma'nosi |
|---|---|---|
| `len("Anora")` | `5` | belgilar soni |
| `"Sal" + "om"` | `"Salom"` | ulash |
| `"ha" * 3` | `"hahaha"` | takrorlash |

`input()` doim `str` qaytargani uchun `*` sonni ko'paytirmaydi, satrni takrorlaydi:

```python
x = input("Son: ")
print(x * 3)
```

```text
Son: 4
444
```

### `bool`

`bool` turida faqat ikki qiymat bor: `True` va `False`. Taqqoslashlar `bool` qaytaradi: `5 > 3` → `True`, `10 == 7` → `False`. `if` aynan shu qiymat bilan ishlaydi.

Boshqa turdagi qiymat ham `if` ichida `True` yoki `False` deb hisoblanadi. `bool()` funksiyasi buni ko'rsatadi:

| Ifoda | Natija | Izoh |
|---|---|---|
| `bool(0)` | `False` | nol |
| `bool(5)` | `True` | noldan farqli son |
| `bool("")` | `False` | bo'sh satr |
| `bool("salom")` | `True` | bo'sh bo'lmagan satr |

Qoida: `0` va bo'sh satr `""` — `False`, qolgan sonlar va satrlar — `True`.

```python
if "0":
    print("Ha")
else:
    print("Yo'q")
```

```text
Ha
```

`"0"` — bo'sh bo'lmagan satr, shuning uchun `True`.

### Turlarni o'zgartirish

Asosiy qoidalar [2-haftada](../week-02/lecture.md#turlarni-ozgartirish) berilgan: `input()` doim `str` qaytaradi, uni `int()`, `float()`, `str()` bilan kerakli turga o'zgartiramiz. Bitta yangi nuqta:

- `int(3.9)` → `3` — `int()` yaxlitlamaydi, kasr qismini tashlab yuboradi. Yaxlitlash uchun `round(3.9)` → `4`.
- `int("3.9")` esa `ValueError` beradi: `int()` matndan faqat butun son yozuvini aylantiradi. Avval `float("3.9")`, keyin kerak bo'lsa `int()`.

## Odatiy xatolar

- **`==` o'rniga `=` yozish.** `if x = 5:` — `SyntaxError`. Taqqoslash uchun `==`.
- **`:` ni unutish.** `if x > 3` (ikki nuqtasiz) — `SyntaxError`.
- **Chekinishni unutish yoki aralashtirish.** `if` ostidagi qatorlar bir xil chekinish bilan yozilishi shart; aks holda `IndentationError`.
- **`elif` o'rniga ketma-ket `if` yozish.** Bir-birini istisno qiladigan holatlar uchun `elif` ishlating, aks holda bir nechta blok bir vaqtda ishlashi mumkin.
- **Shartlar tartibi.** Avval `ball >= 60`, keyin `ball >= 90` yozilsa, 95 ball ham `D` oladi: sharti `True` bo'lgan birinchi blok bajariladi.
- **Chegaralarni adashtirish.** `>` va `>=`, `<` va `<=` farqi: aynan chegaradagi qiymat qaysi tarafga tushishini o'ylab ko'ring.
- **`or` ni noto'g'ri yozish.** `if kun == "shanba" or "yakshanba":` har doim `True` bo'ladi, chunki bo'sh bo'lmagan satr `True` hisoblanadi ([`bool`](#bool) bo'limiga qarang). To'g'risi: `kun == "shanba" or kun == "yakshanba"`.
- **Matn va sonni solishtirish.** `input()` matn qaytaradi: `if input("Yosh: ") >= 18:` — `TypeError`. Avval `int()` ga aylantiring.
- **`return` o'rniga `print`.** `is_even` ichida `print(True)` yozilsa, funksiya `None` qaytaradi va `if is_even(x):` bloki hech qachon bajarilmaydi.
- **Local o'zgaruvchini boshqa funksiyada ishlatish.** `main` ichidagi `name` ni `hello` ko'rmaydi — `NameError`. Qiymatni argument bilan bering.
- **Global o'zgaruvchini funksiya ichida `=` bilan o'zgartirmoqchi bo'lish.** Yangi local o'zgaruvchi yaratiladi, global qiymat o'zgarmaydi. Yangi qiymatni `return` bilan qaytaring.
- **`int(3.9)` ni yaxlitlaydi deb o'ylash.** Natija `3`. Yaxlitlash uchun `round()`.
