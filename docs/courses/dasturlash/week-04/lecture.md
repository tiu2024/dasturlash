# 4-hafta. Looplar va stringlar

Ma'ruza taqdimoti: [Looplar va stringlar (PPTX)](../../../downloads/dasturlash/week-04/looplar-va-stringlar.pptx)

Bu haftaning amaliy qismi: [amaliyot](practice.md).

## Nima uchun loop kerak

Ba'zan bir ishni qayta-qayta qilish kerak. Masalan, 1 dan 100 gacha sonlarni chiqarish:

```python
print(1)
print(2)
print(3)
# ... yana 97 ta qator?
```

100 ta `print` yozish mumkin, lekin 1000 ta bo'lsa-chi? Yana bir holat: telefon PIN kod to'g'ri kiritilguncha so'raydi. Necha marta so'rashi oldindan noma'lum.

**Loop** (takrorlash) — bir ishni kodni ko'chirmasdan, kerakli marta takrorlatish usuli. Budilnik kabi: siz "o'chirish" tugmasini bosmaguncha u qayta-qayta jiringlayveradi.

Python'da ikkita loop bor:

- `while` — necha marta takrorlash oldindan **noma'lum** bo'lsa (PIN to'g'ri kiritilguncha);
- `for` — necha marta takrorlash oldindan **ma'lum** bo'lsa (har bir shahar uchun, roppa-rosa 10 marta).

### Loop qanday ishlaydi

Har bir loop shu tartibda ishlaydi:

1. **Boshlash** — bir marta, loop boshlanishidan oldin.
2. **Shart** — har aylanish boshida tekshiriladi. Aylanish — blokning bir marta bajarilishi.
3. Shart `True` bo'lsa: **blok** bajariladi va yana shartga qaytiladi.
4. Shart `False` bo'lsa: loop tugaydi va loopdan keyingi qatorga o'tiladi.

Muhim: shart **faqat aylanish boshida** tekshiriladi. Blok o'rtasida shart `False` bo'lib qolsa ham, blok oxirigacha bajariladi.

## `while` loop

### Loopning uch qismi

```python
i = 0               # 1. boshlash
while i < 3:        # 2. shart
    print("Salom!")
    i += 1          # 3. yangilash
```

```text
Salom!
Salom!
Salom!
```

- **Boshlash** — loopdan oldin, faqat bir marta: `i = 0`.
- **Shart** — har aylanish boshida tekshiriladi: `i < 3`.
- **Yangilash** — loopni tugashga yaqinlashtiradi: `i += 1`. Bu `i = i + 1` ning qisqa yozilishi. Yangilash unutilsa, loop cheksiz bo'ladi.

Dasturchilar odatda 0 dan sanaydi: `i = 0` va `i < 3` — roppa-rosa uch marta.

`while` dan keyin `:` qo'yiladi va blok `if` dagidek 4 ta probel chekinish bilan yoziladi ([3-haftaga](../week-03/lecture.md#if) qarang).

### Qadamma-qadam kuzatish

Loop qanday ishlashini jadvalda **kuzatamiz**: har tekshiruvda `i` nima bo'ladi, shart qanday, blok nima qiladi.

| Tekshiruv | `i` | `i < 3` | Natija |
|---|---|---|---|
| 1 | 0 | `True` | "Salom!", `i` → 1 |
| 2 | 1 | `True` | "Salom!", `i` → 2 |
| 3 | 2 | `True` | "Salom!", `i` → 3 |
| 4 | 3 | `False` | loop tugaydi |

Shart 4 marta tekshirildi, blok esa 3 marta bajarildi. Oxirgi tekshiruv `False` bo'lgani uchun loop to'xtaydi.

### `while True` va `break`

Necha marta takrorlanishi noma'lum bo'lsa, shart sifatida doim `True` yoziladi va loopdan `break` bilan chiqiladi. `break` — loopni darhol tugatadi.

```python
while True:
    kod = input("PIN: ")
    if kod == "1234":
        break
    print("Noto'g'ri, qayta urining")
print("Telefon ochildi!")
```

```text
PIN: 0000
Noto'g'ri, qayta urining
PIN: 1234
Telefon ochildi!
```

Shart doim `True`, shuning uchun loopni faqat `break` to'xtatadi. `break` bo'lmasa loop cheksiz aylanadi.

### Cheksiz loop

Loop to'xtamasa, dastur "qotib qoladi". Buning ikki sababi bor.

**1. Yangilash unutilgan:**

```python
son = 1
while son < 10:
    print(son)
    # son += 1 yo'q!
```

```text
1
1
1
...
```

`son` hech qachon o'zgarmaydi, shart doim `True`, shuning uchun `1` abadiy chiqaveradi.

**2. Chegara sakrab o'tilgan:**

```python
son = 3
while son != 10:
    son += 2
```

`son` ning qiymatlari: 5, 7, 9, 11, 13, ... Hammasi toq son, shuning uchun u `10` ga hech qachon teng bo'lmaydi va shart `True` bo'lib qoladi.

Cheksiz loopni **Ctrl + C** bilan to'xtatish mumkin. Xavfsizroq yo'l: `!=` o'rniga `<` yoki `<=` ishlating.

### SAVOL: telefon necha foiz bo'ladi?

Telefon 85% da. Har daqiqada u 4% quvvat oladi. Natijani ishga tushirmasdan toping:

```python
foiz = 85
while foiz < 100:
    foiz += 4
print(foiz)
```

```text
101
```

**Javob: 101.** Qiymatlar: 85 → 89 → 93 → 97 → 101. `97` da shart hali `True` (97 < 100), shuning uchun yana 4 qo'shiladi. Shart faqat aylanish boshida tekshiriladi, shuning uchun loop `100` da "o'zi to'xtab qolmaydi".

### SAVOL: Gauss xato qildimi?

Maqsad: 1 dan 100 gacha bo'lgan sonlar yig'indisi (to'g'ri javob 5050).

```python
i = 1
s = 0
while i < 100:
    s += i
    i += 1
print(s)
```

```text
4950
```

**Javob: 4950.** Shart `i < 100`, shuning uchun `i = 100` bo'lganda loop tugaydi va `100` qo'shilmay qoladi: 1 + 2 + ... + 99 = 4950. To'g'risi `i <= 100`: shunda natija `5050`.

Bu **off-by-one** xatosi — chegarani bittaga adashtirish. Ko'pchilik `5050` deb javob beradi, chunki Gauss javobini yodlagan: kodni emas, maqsadni o'qigan. Har doim kodning o'zini o'qing.

## `for` loop

### `for` — har bir element uchun

`for` har bir elementni navbat bilan oladi. Davomatga o'xshaydi: o'qituvchi jurnaldagi har bir ismni bittadan o'qiydi.

```python
shaharlar = ["Toshkent", "Samarqand", "Buxoro"]
for shahar in shaharlar:
    print(shahar)
```

```text
Toshkent
Samarqand
Buxoro
```

Kvadrat qavs ichidagi bir nechta qiymat — **ro'yxat** (list). Hozircha uni shunchaki elementlar ketma-ketligi deb biling, ro'yxatlar haqida keyingi darslarda batafsil gaplashamiz.

Har aylanishda `shahar` navbatdagi elementga teng bo'ladi. `while` dagi boshlash, shart va yangilashni `for` o'zi bajaradi.

### `range()`

Sonlar ketma-ketligini `range()` beradi: `range(start, stop, qadam)`. `stop` ketma-ketlikka **kirmaydi**.

| Yozuv | Sonlar | Izoh |
|---|---|---|
| `range(5)` | 0 1 2 3 4 | 0 dan boshlanadi |
| `range(1, 6)` | 1 2 3 4 5 | `start` va `stop` |
| `range(0, 10, 2)` | 0 2 4 6 8 | qadam 2 |
| `range(5, 0, -1)` | 5 4 3 2 1 | teskari sanoq |
| `range(5, 1)` | (bo'sh) | hech narsa |

```python
for i in range(1, 4):
    print(i)
```

```text
1
2
3
```

`range(5, 1)` da qadam yozilmagan, u `+1` bo'ladi. 5 dan oshib borib 1 ga yetib bo'lmaydi, shuning uchun ketma-ketlik bo'sh. Bu xato bermaydi, shunchaki hech narsa qilmaydi.

`range(5)` aynan 5 marta aylantiradi — sanab ko'rish oson. Sanoq raqami kerak bo'lmasa, o'zgaruvchi o'rniga `_` yoziladi:

```python
for _ in range(3):
    print("Salom!")
```

```text
Salom!
Salom!
Salom!
```

### `while` yoki `for`?

| `while` | `for` |
|---|---|
| Necha marta — oldindan noma'lum. | Ketma-ketlik yoki aniq son. |
| PIN to'g'ri kiritilguncha, `-1` kiritilguncha, pul yetguncha | Har bir shahar, har bir harf, roppa-rosa 10 marta |
| `while pul < narx:` | `for _ in range(10):` |

### SAVOL: raketa uchadimi?

```python
for i in range(3, 0):
    print(i)
print("Start!")
```

```text
Start!
```

**Javob: faqat "Start!".** Qadam yozilmagani uchun u `+1` bo'ladi, 3 dan oshib borib 0 ga yetib bo'lmaydi. `range` bo'sh, loop bir marta ham aylanmaydi, xato ham chiqmaydi. Python o'zi teskari sanamaydi. To'g'ri yozuv `range(3, 0, -1)`:

```python
for i in range(3, 0, -1):
    print(i)
print("Start!")
```

```text
3
2
1
Start!
```

## Satrlar

### Index

**Satr** (string, `str`) — tizilgan belgilar, har birining o'z raqami bor. Bu raqam **index** deb ataladi. Index chapdan boshlanadi va **0** dan sanaladi. Manfiy index o'ngdan sanaydi: `-1` — doim oxirgi belgi.

`"Buxoro"` satri:

| Belgi | B | u | x | o | r | o |
|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| Manfiy index | -6 | -5 | -4 | -3 | -2 | -1 |

`"Buxoro"` da 6 ta belgi bor, lekin oxirgi index 5: oxirgi index doim `len(satr) - 1`.

### `len()` va index

Belgini raqami bo'yicha kvadrat qavs bilan olamiz: `satr[index]`.

```python
shahar = "Buxoro"
print(len(shahar))
print(shahar[0])
print(shahar[-1])
print(shahar[len(shahar)])
```

```text
6
B
o
IndexError: string index out of range
```

Oxirgi qator xato beradi: `shahar[6]` mavjud emas, chunki oxirgi index 5. Oxirgi belgi uchun `shahar[len(shahar) - 1]` yoki shunchaki `shahar[-1]` yozing. `len()` bo'sh joylarni ham sanaydi: `len("Yangi yil")` — `9`.

### Slice: satrdan bo'lak olish

`satr[a:b]` — `a` dan `b` gacha bo'lak. `a` bo'lakka **kiradi**, `b` **kirmaydi**.

```python
raqam = "+998901234567"
print(raqam[:4])    # davlat kodi
print(raqam[4:6])   # operator
print(raqam[6:])    # raqamning o'zi
print(raqam[-4:])   # oxirgi 4 ta belgi
```

```text
+998
90
1234567
4567
```

- `a` yozilmasa — boshidan;
- `b` yozilmasa — oxirigacha;
- bo'lak uzunligi: `b - a`. Masalan, `raqam[4:6]` — 4 va 5-indexdagi belgilar, ya'ni `"90"`.

`stop` kirmaydi degan qoida `range()` bilan bir xil.

### `in` va `find()`

```python
email = "anora@mail.uz"
print("@" in email)
print(email.find("@"))
print(email.find("#"))
print(email[:email.find("@")])
```

```text
True
5
-1
anora
```

- `a in s` — faqat `True` yoki `False` beradi, joyini aytmaydi.
- `s.find(a)` — birinchi uchragan joyning indexini beradi. Topilmasa, `-1`. `find` — **metod** ([2-haftada](../week-02/lecture.md#satrlar-bilan-ishlash) metodlar bilan tanishgansiz): satrdan keyin nuqta qo'yib chaqiriladi.

Ikkalasi ham katta-kichik harfni farqlaydi: `"Dars"` va `"dars"` har xil.

Oxirgi qator ikki g'oyani birlashtiradi: `find` `@` ning o'rnini topadi (`5`), slice esa boshidan shu o'ringacha kesadi — login chiqadi.

### Satr ustida loop

`for` satrning har bir harfini bittadan beradi. Misol: so'zni teskari yozamiz.

```python
soz = "kitob"
teskari = ""      # bo'sh satr
for h in soz:
    teskari = h + teskari
print(teskari)
```

```text
botik
```

Har bir yangi harf oldinga yopishtiriladi:

| `h` | `teskari` |
|---|---|
| k | k |
| i | ik |
| t | tik |
| o | otik |
| b | botik |

`teskari + h` deb yozilsa, so'z o'zgarmay qoladi (`kitob`). Shu g'oya bilan so'z **palindrom** (ikki tomondan bir xil o'qiladigan, masalan `kiyik`) ekanini tekshirish mumkin: `teskari == soz`.

### SAVOL: qaysi ikki harf chiqadi?

```python
s = "Termiz"
print(s[-2] + s[0])
```

```text
iT
```

**Javob: `iT`.** `-1` — oxirgi harf `z`, `-2` — undan oldingisi `i`. `s[0]` — `T`. `+` ularni yopishtiradi: `"i" + "T"`. Manfiy index `-1` dan boshlanishini unutmang: `-2` — "oxirgisi" emas, "oxiridan ikkinchi".

## `break` va `continue`

- `continue` — shu aylanishning qolganini tashlaydi, loop davom etadi;
- `break` — loopni butunlay tugatadi, keyingi qatorga o'tiladi.

Lift 13-qavatda to'xtamaydi:

```python
for qavat in range(10, 16):
    if qavat == 13:
        continue
    print(f"{qavat}-qavat")
```

```text
10-qavat
11-qavat
12-qavat
14-qavat
15-qavat
```

([f-string](../week-02/lecture.md#qiymatlarni-birga-chiqarish) — `{qavat}` o'rniga uning qiymati yoziladi.)

`continue` o'rniga `break` yozilsa, 13 da loop tugaydi va faqat 10, 11, 12-qavat chiqadi.

### SAVOL: nima chiqadi?

```python
i = 0
while i < 5:
    if i == 2:
        continue
    i += 1
print(i)
```

**Javob: hech narsa chiqmaydi, loop cheksiz aylanadi.** `i` 2 ga yetganda `continue` aylanishning qolganini, jumladan `i += 1` ni ham tashlab o'tadi. `i` 2 da qotib qoladi, shart doim `True`, shuning uchun `print(i)` ga navbat hech qachon kelmaydi.

`for` da `continue` faqat joriy qiymatni o'tkazib yuboradi. `while` da esa yangilash tashlanib ketishi mumkin. Saboq: `while` ichida `continue` ishlatsangiz, yangilash `continue` dan **oldin** turishi kerak.

## Ichma-ich looplar

Loop ichida yana loop yozish mumkin. Soat misoli: daqiqa mili (`j`) to'liq aylangandan keyin soat mili (`i`) bir qadam yuradi.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```

```text
1 2 3 
2 4 6 
3 6 9 
```

Tartib: `i = 1` da `j` 1, 2, 3 ni to'liq o'tadi. Keyin `i = 2` bo'ladi va `j` yana 1 dan boshlanadi. Ichki aylanishlar soni: 3 × 3 = 9.

- `print(..., end=" ")` odatdagi yangi qatorga o'tish o'rniga bo'sh joy qo'yadi, shuning uchun sonlar bir qatorda chiqadi.
- Bo'sh `print()` qatorni tugatadi.

Ichki loopdagi `break` faqat **ichki** loopni to'xtatadi, tashqi loop davom etadi.

### SAVOL: nechta yulduz chiqadi?

```python
for i in range(2):
    for j in range(5):
        if j == 2:
            break
        print("*", end="")
```

```text
****
```

**Javob: 4 ta.** Har bir tashqi aylanishda ichki loop `j = 0` va `j = 1` da yulduz chiqaradi, `j = 2` da `break` bilan to'xtaydi. `break` faqat ichki loopni tugatadi, tashqi loop 2 marta ishlaydi: 2 × 2 = 4.

## Xulosa

```python
while shart:                  # necha marta — noma'lum
    ...

for x in range(a, b, qadam):  # b kirmaydi
    ...
```

Satr uchun: `s[0]`, `s[-1]`, `s[a:b]`, `len(s)`, `"a" in s`, `s.find("a")`. Loop ichida: `break`, `continue`.

1. Loop: boshlash → shart → yangilash.
2. `range` va slice'da `stop` kirmaydi.
3. Index 0 dan boshlanadi; oxirgisi — `len(s) - 1` yoki `-1`.
4. `continue` — keyingi aylanish, `break` — loopdan chiqish.

## Odatiy xatolar

- **Yangilashni unutish.** `while i < 10:` ichida `i += 1` yo'q bo'lsa, loop cheksiz. Blok oxiriga `i += 1` qo'shing.
- **`input()` ni loopdan tashqarida yozish.** Qiymat bir marta so'raladi va loop cheksiz aylanadi, qayta so'ramaydi. `input()` ni loop ichiga oling.
- **Chegarani sakrab o'tish.** `while son != 10:` da `son` 10 ga teng bo'lmasa, loop to'xtamaydi. `!=` o'rniga `<` yoki `<=` ishlating.
- **Off-by-one.** `while i < 100:` da 100 qo'shilmaydi. `range(1, 10)` da ham `10` yo'q: oxirgi son chiqishi uchun `stop` ni bittaga oshiring — `range(1, 11)`.
- **Teskari sanoqda qadamni yozmaslik.** `range(3, 0)` bo'sh. To'g'risi: `range(3, 0, -1)`.
- **`s[len(s)]`.** `IndexError`. Oxirgi belgi: `s[-1]` yoki `s[len(s) - 1]`.
- **`while` ichida `continue` yangilashdan oldin.** `i += 1` tashlab o'tiladi, loop cheksiz. Yangilashni `continue` dan oldinga qo'ying.
- **Ichki `break` butun dasturni to'xtatadi deb o'ylash.** U faqat ichki loopni tugatadi.
- **Katta va kichik harfni aralashtirish.** `"A"` va `"a"` har xil belgi: `"Andijon"` da `h == "a"` sharti bilan sanasangiz, `0` chiqadi.

Cheksiz loop bo'lsa — **Ctrl + C**. Xato xabarini pastdan yuqoriga o'qing: oxirgi qator — xato turi, undan yuqorisi — qaysi qatorda.
