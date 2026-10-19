# 5-hafta. Ro'yxatlar va kortejlar

Ma'ruza taqdimoti: [Ro'yxatlar va kortejlar (PPTX)](../../../downloads/dasturlash/week-05/royxatlar-va-kortejlar.pptx)

Bu haftada bir nechta qiymatni bitta nom ostida saqlashni o'rganamiz: **ro'yxat** (list), **kortej** (tuple) va **to'plam** (set). Eng muhim qismi — [havolalar](#havolalar-bitta-royxat-ikki-nom): ikki o'zgaruvchi bitta ro'yxatga ishora qilganda nima bo'ladi.

## Kolleksiyalarsiz qanday bo'lardi?

Bugungi mavzuning nima uchun kerakligini uchta muammoda ko'ramiz.

### 1. Ko'p qiymat uchun ko'p nom

Guruhda 30 ta talaba bor. Hammasining ismini chiqarish uchun nima yozamiz?

```python
ism1 = "Ali"
ism2 = "Vali"
ism3 = "Hasan"
print(ism1)
print(ism2)
print(ism3)
# ... yana 27 ta ism va 27 ta print
```

Har bir ism uchun alohida o'zgaruvchi va alohida `print` kerak. `for` bilan ham aylanib chiqib bo'lmaydi: `ism1`, `ism2`, `ism3` alohida nomlar, ularni hech narsa bog'lamaydi. Guruh 31 kishi bo'lsa, kodni qayta yozishga to'g'ri keladi.

### 2. Qiymatlar soni oldindan noma'lum

Foydalanuvchi 70, 85 va 90 ballni kiritsa, bu kod nimani chiqaradi?

```python
for i in range(3):
    ball = int(input("Ball: "))
print(ball)
```

```text
Ball: 70
Ball: 85
Ball: 90
90
```

**Javob: 90.** Har yangi qiymat eskisini o'chiradi: o'zgaruvchi faqat bitta qiymat saqlaydi. Oldingi ballar yo'qoldi. Necha ball kiritilishini oldindan bilmaymiz, dastur ishlayotganda yangi o'zgaruvchi ham yarata olmaymiz.

### 3. Funksiyaning parametrlari soni qat'iy

[3-haftada](../week-03/lecture.md) funksiyalarni o'rgandik. Uch ballning o'rtachasini hisoblaydigan funksiya:

```python
def ortacha(b1, b2, b3):
    return (b1 + b2 + b3) / 3


print(ortacha(70, 85, 90))
```

```text
81.66666666666667
```

Funksiya aynan uchta ball kutadi. To'rtta ball bo'lsa, parametr qo'shib formulani qayta yozish kerak. Yuz ball bo'lsa, bu umuman mumkin emas.

### Yechim: kolleksiya

Uchala muammoning ildizi bitta: ko'p qiymatni bitta nom ostida saqlashning usuli yo'q. **Kolleksiya** shuni hal qiladi. Bugun uch turi bilan tanishamiz:

| Kolleksiya | Qisqacha | Misol |
|---|---|---|
| ro'yxat (list) | tartibli, o'zgaradi | `[1, 2, 3]` |
| kortej (tuple) | tartibli, o'zgarmaydi | `(1, 2, 3)` |
| to'plam (set) | takrorsiz, tartibsiz | `{1, 2, 3}` |

Dars oxirida bu jadvalga yana qaytamiz.

## Ro'yxat

### Ro'yxat yaratish

**Ro'yxat** — kvadrat qavs ichida, vergul bilan ajratib yozilgan qiymatlar. Ro'yxatdagi har bir qiymat **element** deb ataladi. Elementlar sonini satrlardagidek `len()` topadi.

```python
mevalar = ["olma", "anor", "uzum"]
print(mevalar)
print(len(mevalar))
bosh = []
print(len(bosh))
```

```text
['olma', 'anor', 'uzum']
3
0
```

`[]` — bo'sh ro'yxat: unda hech narsa yo'q, uzunligi `0`. Ro'yxat nomini odatda ko'plikda qo'yamiz: `mevalar`, `ismlar`.

### Indeks va kesim

[4-haftada](../week-04/lecture.md#index) satrlar uchun o'rganilgan qoidalar ro'yxatda ham xuddi shunday ishlaydi: indeks `0` dan boshlanadi, `-1` — oxirgi element, kesimda oxirgi indeks kirmaydi ([slice](../week-04/lecture.md#slice-satrdan-bolak-olish)).

```python
mevalar = ["olma", "anor", "uzum", "behi"]
print(mevalar[0])
print(mevalar[-1])
print(mevalar[1:3])
```

```text
olma
behi
['anor', 'uzum']
```

Kesim yangi ro'yxat beradi. Yangi qoida yo'q.

### `for` va `in`

[`for`](../week-04/lecture.md#for-har-bir-element-uchun) har aylanishda ro'yxatning keyingi elementini beradi. `in` elementning ro'yxatda bor-yo'qligini `True` yoki `False` bilan aytadi ([`in`](../week-04/lecture.md#in-va-find) satrlarda ham shunday).

```python
mevalar = ["olma", "anor", "uzum"]
for meva in mevalar:
    print(meva)
print("anor" in mevalar)
print("nok" in mevalar)
```

```text
olma
anor
uzum
True
False
```

### Ro'yxat o'zgaradi, satr esa yo'q

Ro'yxat elementiga indeks bo'yicha yangi qiymat berish mumkin:

```python
narxlar = [12000, 18000, 10900]
narxlar[0] = 13000
print(narxlar)
```

```text
[13000, 18000, 10900]
```

Satr bilan bunday qilib bo'lmaydi:

```python
soz = "olma"
soz[0] = "a"
```

```text
TypeError: 'str' object does not support item assignment
```

Ro'yxat — o'zgaradigan kolleksiya, satr esa o'zgarmaydi. Satrni o'zgartirmoqchi bo'lsak, yangi satr yasaymiz.

### SAVOL: nima chiqadi?

```python
mevalar = ["olma", "anor", "uzum"]
print(mevalar[3])
```

```text
IndexError: list index out of range
```

**Javob: `IndexError`.** Ro'yxatda 3 ta element bor, indekslar `0`, `1`, `2`. Indeks `3` mavjud emas. Xato xabari "indeks ro'yxat chegarasidan tashqarida" degani. Oxirgi indeks doim `len(ro'yxat) - 1` yoki shunchaki `-1`.

## Qo'shish va o'chirish

### `append`: oxiriga qo'shish

`append` — **metod**: ro'yxatdan keyin nuqta qo'yib chaqiriladi ([2-haftada](../week-02/lecture.md#satrlar-bilan-ishlash) satr metodlari bilan tanishgansiz). U elementni doim ro'yxat oxiriga qo'shadi.

```python
mehmonlar = []
mehmonlar.append("Ali")
mehmonlar.append("Vali")
print(mehmonlar)
```

```text
['Ali', 'Vali']
```

Bo'sh ro'yxatdan boshlab, uni qadam-baqadam to'ldirish mumkin. Dars boshidagi ikkinchi muammoning (ballar yo'qolib borishi) javobi shu: ballarni `append` bilan yig'ib boramiz.

### `insert`: tanlangan o'ringa qo'yish

`insert(indeks, qiymat)` yangi elementni shu indeksga qo'yadi, undan keyingilar o'ngga suriladi. Navbatga o'xshaydi: kimdir o'rtaga kirsa, orqadagilar bir qadam orqaga ketadi.

```python
mehmonlar = ["Ali", "Vali"]
mehmonlar.insert(0, "Hasan")
print(mehmonlar)
mehmonlar.insert(2, "Olim")
print(mehmonlar)
```

```text
['Hasan', 'Ali', 'Vali']
['Hasan', 'Ali', 'Olim', 'Vali']
```

### `pop` va `del`: indeks bo'yicha o'chirish

- `pop(indeks)` elementni ro'yxatdan oladi va **qaytaradi**, shuning uchun uni o'zgaruvchiga saqlash mumkin. Indekssiz `pop()` oxirgi elementni oladi.
- `del royxat[indeks]` elementni shunchaki o'chiradi, hech narsa qaytarmaydi.

```python
bozorlik = ["yog'", "un", "piyoz", "banan"]
mahsulot = bozorlik.pop(3)
print(mahsulot)
print(bozorlik)
del bozorlik[0]
print(bozorlik)
```

```text
banan
["yog'", 'un', 'piyoz']
['un', 'piyoz']
```

Ikkalasida ham o'rin raqami (indeks) kerak.

### `remove`: qiymat bo'yicha o'chirish

Elementning o'rnini bilmasak, qiymatini aytamiz. `remove` faqat **birinchi** topilgan elementni o'chiradi.

```python
hayvonlar = ["it", "mushuk", "mushuk"]
hayvonlar.remove("mushuk")
print(hayvonlar)
```

```text
['it', 'mushuk']
```

Ro'yxatda ikkita `"mushuk"` bor edi, lekin faqat birinchisi o'chdi. Ikkinchisini o'chirish uchun `remove` ni yana chaqirish kerak.

### O'chirishdan oldin `in` bilan tekshiring

Ro'yxatda yo'q qiymatni `remove` bilan o'chirmoqchi bo'lsak, Python `ValueError` beradi va dastur to'xtaydi. Avval `in` bilan tekshirish xavfsiz ([shartlarni](../week-03/lecture.md#if) bilasiz):

```python
hayvonlar = ["it", "sigir"]
if "mushuk" in hayvonlar:
    hayvonlar.remove("mushuk")
else:
    print("Mushuk ro'yxatda yo'q")
hayvonlar.remove("mushuk")
```

```text
Mushuk ro'yxatda yo'q
ValueError: list.remove(x): x not in list
```

Oxirgi qator tekshiruvsiz chaqirilgan: u xato beradi.

### SAVOL: qaysi yozuv to'g'ri?

`bozorlik` ro'yxatidan `"banan"` ni o'chirmoqchisiz, lekin uning o'rnini bilmaysiz. Qaysi yozuv to'g'ri?

- A. `bozorlik.append("banan")`
- B. `bozorlik.remove("banan")`
- C. `bozorlik.pop("banan")`
- D. `del bozorlik["banan"]`

**Javob: B.** `remove` qiymat bo'yicha o'chiradi. `pop` va `del` indeks, ya'ni son kutadi: ularga matn berilsa, xato chiqadi. `append` esa o'chirmaydi, qo'shadi.

## Kortej

### O'zgarmaydigan ro'yxat

**Kortej** — yumaloq qavs bilan yoziladigan, o'zgarmaydigan ro'yxat. Indeks, `len` va `for` ro'yxatdagidek ishlaydi. O'zgartirib bo'lmaydi: qiymat berish ham, `append` ham, `remove` ham ishlamaydi.

```python
koordinata = (41.3, 69.2)
print(koordinata[0])
print(len(koordinata))
koordinata[0] = 0
```

```text
41.3
2
TypeError: 'tuple' object does not support item assignment
```

Bu xato satrdagi xatoga o'xshash: ikkalasi ham o'zgarmaydi.

### Kortej qachon kerak

O'zgarmasligi kerak bo'lgan ma'lumotni kortejga yozing: masalan, koordinata `(41.3, 69.2)`. Uni tasodifan o'zgartirib qo'ysangiz, Python darrov xato beradi va xatoni o'sha zahoti topasiz. O'zgaradigan ma'lumot (mehmonlar, bozorlik) uchun ro'yxat qulay.

## Havolalar: bitta ro'yxat, ikki nom

### SAVOL: `b = a` nima qiladi?

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

```text
[1, 2, 3, 4]
```

**Javob: `[1, 2, 3, 4]`.** Ko'pchilik `[1, 2, 3]` deb o'ylaydi, chunki sonlarda shunday bo'ladi: [2-haftadagi](../week-02/lecture.md#qiymatni-ozgartirish) `a = 5`, `b = a`, `b = 6` misolida `a` o'zgarmaydi. Ro'yxatlarda esa boshqacha: `b = a` ro'yxatning nusxasini yasamaydi, `a` ham, `b` ham **bitta** ro'yxatga ishora qiladi.

### Ikki nom, bitta ro'yxat

Ro'yxat katta obyekt: o'zgaruvchi uni emas, unga **havola**ni (kompyuter xotirasidagi o'rniga ko'rsatkichni) saqlaydi. `b = a` havolani nusxalaydi, ro'yxatni emas. Bitta odamning ikki laqabiga o'xshaydi: kimdir uni bir laqab bilan o'zgartirsa, ikkinchi laqab ostida ham o'zgargan bo'ladi.

```python
a = [1, 2, 3]
b = a
print(id(a) == id(b))
b.append(4)
print(a)
print(b)
```

```text
True
[1, 2, 3, 4]
[1, 2, 3, 4]
```

`id()` obyektning xotiradagi manzilini beradi. `True` — ikkala nom bir joydagi ro'yxatga ishora qiladi. Sonlar va satrlar o'zgarmaydi, shuning uchun ular bilan bunday muammo bo'lmaydi.

### `a[:]`: haqiqiy nusxa

Kesim yangi ro'yxat yasaydi ([4-haftadan](../week-04/lecture.md#slice-satrdan-bolak-olish) eslang). Boshi ham, oxiri ham yozilmasa, kesim butun ro'yxatni oladi: bu nusxa.

```python
a = [1, 2, 3]
b = a[:]
print(id(a) == id(b))
b.append(4)
print(a)
print(b)
```

```text
False
[1, 2, 3]
[1, 2, 3, 4]
```

Endi `b` alohida ro'yxat, `id` lar har xil, `a` esa o'zgarmadi. Ro'yxatning haqiqiy nusxasi kerak bo'lsa, `[:]` ishlating.

### Funksiyaga berilgan ro'yxat

Argument sifatida ro'yxat berilsa, funksiya nusxani emas, ro'yxatning o'zini oladi: `royxat` va `sonlar` bitta ro'yxatga ishora qiladi.

```python
def qosh(royxat):
    royxat.append(10)


sonlar = [1, 2, 3]
qosh(sonlar)
print(sonlar)
```

```text
[1, 2, 3, 10]
```

Funksiya hech narsa qaytarmadi, lekin tashqaridagi `sonlar` o'zgardi. Bu foydali bo'lishi mumkin, lekin xavfli ham.

### `sorted()` va `sort()`

Ikkalasi ham ro'yxatni kichikdan kattaga tartiblaydi, lekin ular har xil ishlaydi:

- `sorted(sonlar)` — yangi tartiblangan ro'yxat qaytaradi, asl ro'yxat o'zgarmaydi;
- `sonlar.sort()` — asl ro'yxatning o'zini tartiblaydi va hech narsa qaytarmaydi.

```python
sonlar = [4, 1, 3, 2]
print(sorted(sonlar))
print(sonlar)
sonlar.sort()
print(sonlar)
```

```text
[1, 2, 3, 4]
[4, 1, 3, 2]
[1, 2, 3, 4]
```

### SAVOL: funksiyadan keyin ro'yxat qanday bo'ladi?

```python
def ikkinchi_kichik(royxat):
    royxat.sort()
    return royxat[1]


sonlar = [4, 1, 3, 2]
print(ikkinchi_kichik(sonlar))
print(sonlar)
```

```text
2
[1, 2, 3, 4]
```

**Javob: `2` va `[1, 2, 3, 4]`.** Funksiya ikkinchi eng kichik sonni topdi, lekin `sort()` bilan `sonlar` ro'yxatini ham tartiblab yubordi. Funksiyani chaqirgan odam buni kutmagan edi. Bunday kutilmagan o'zgarish **yon ta'sir** (*side effect*) deyiladi. Dastur kattalashganda bunday xatolarni topish qiyin.

### Yon ta'sirsiz funksiya

`sorted()` yangi ro'yxat yasaydi. Funksiya o'sha nusxani tartiblaydi, asl ro'yxatga tegmaydi:

```python
def ikkinchi_kichik(royxat):
    nusxa = sorted(royxat)
    return nusxa[1]


sonlar = [4, 1, 3, 2]
print(ikkinchi_kichik(sonlar))
print(sonlar)
```

```text
2
[4, 1, 3, 2]
```

Qoida: funksiya o'ziga berilgan ro'yxatni o'zgartirmasin, agar aynan shu uning vazifasi bo'lmasa. Kerak bo'lsa, `[:]` yoki `sorted()` bilan nusxa oling.

### Dars boshidagi uchinchi muammoning yechimi

Ro'yxat parametr bo'lsa, funksiya istalgan sondagi ball uchun ishlaydi: bitta parametr — butun ro'yxat, ichida `for` bilan yig'indini hisoblab, uzunlikka bo'lamiz.

```python
def ortacha(ballar):
    jami = 0
    for ball in ballar:
        jami += ball
    return jami / len(ballar)


print(ortacha([70, 85, 90]))
print(ortacha([70, 85, 90, 60]))
```

```text
81.66666666666667
76.25
```

Funksiyani uch ball uchun ham, to'rt ball uchun ham, yuz ball uchun ham o'zgartirish shart emas.

## To'plam

### Takrorlarni saqlamaydi

**To'plam** — figurali qavs ichidagi qiymatlar. U har bir qiymatni faqat bir marta saqlaydi.

```python
shaharlar = {"Toshkent", "Samarqand", "Toshkent"}
print(len(shaharlar))
bosh = set()
print(len(bosh))
```

```text
2
0
```

`"Toshkent"` ikki marta yozilgan, lekin to'plamda bir marta qoladi, shuning uchun uzunlik `2`. Bo'sh to'plam `set()` bilan yaratiladi. Bo'sh figurali qavs `{}` to'plam emas: u boshqa kolleksiyani yaratadi, uni keyinroq o'rganamiz. To'plamni to'liq chiqarmadik: undagi qiymatlar tartibi o'zgarib turishi mumkin.

### Tartib yo'q, indeks ham yo'q

To'plamda "birinchi element" degan tushuncha yo'q, shuning uchun `[0]`, `[-1]` va kesim ishlamaydi.

```python
shaharlar = {"Toshkent", "Samarqand"}
print(shaharlar[0])
```

```text
TypeError: 'set' object is not subscriptable
```

"Not subscriptable" — "kvadrat qavsni qo'llab-quvvatlamaydi" degani. To'plam bilan `for` va `in` ishlaydi, faqat tartib kafolatlanmagan.

### `add`, `discard`, `remove`

- `add` — qo'shadi. Takroriy qo'shish hech narsani o'zgartirmaydi.
- `in` — tekshiradi.
- `discard` — o'chiradi; qiymat yo'q bo'lsa, xato bermaydi.
- `remove` — o'chiradi; qiymat yo'q bo'lsa, `KeyError` beradi.

```python
shaharlar = {"Toshkent", "Samarqand"}
shaharlar.add("Buxoro")
shaharlar.add("Buxoro")
print(len(shaharlar))
print("Buxoro" in shaharlar)
shaharlar.discard("Xiva")
shaharlar.remove("Xiva")
```

```text
3
True
KeyError: 'Xiva'
```

Ro'yxatdagi `remove` yo'q qiymatda `ValueError` bergan edi: xato turi boshqa, lekin g'oya bir xil.

### `set()` bilan takrorlarni olib tashlash

To'plamning asosiy qo'llanilishi shu. Ro'yxatda 6 ta kelish yozilgan, lekin odam nechta?

```python
kelganlar = ["Ali", "Vali", "Ali", "Hasan", "Vali", "Ali"]
print(len(kelganlar))
print(len(set(kelganlar)))
```

```text
6
3
```

`set(kelganlar)` ro'yxatdan takrorlarsiz to'plam yasaydi, uning uzunligi — turli odamlar soni. Asl ro'yxat o'zgarmaydi.

### SAVOL: nechta element?

```python
print(len({1, 2, 2, 3, 3, 3}))
```

```text
3
```

**Javob: `3`.** Takrorlar bir marta sanaladi: faqat `1`, `2` va `3` qoladi. Bir xil qiymatlar bilan to'ldirilgan `[1, 2, 2, 3, 3, 3]` ro'yxati uchun esa `len` `6` bo'lardi.

## Xulosa

| | Ro'yxat | Kortej | To'plam |
|---|---|---|---|
| Qavs | `[ ]` | `( )` | `{ }` |
| O'zgaradi | ha | yo'q | ha |
| Tartib va indeks | bor | bor | yo'q |
| Takrorlar | mumkin | mumkin | yo'q |

1. Ro'yxat ko'p qiymatni bitta nom ostida saqlaydi va indeks bilan o'zgaradi.
2. `append`, `insert` qo'shadi; `pop`, `del` indeks bo'yicha, `remove` qiymat bo'yicha o'chiradi.
3. Kortej o'zgarmaydi; to'plam takrorlarni saqlamaydi.
4. `b = a` nusxa emas, ikkinchi nom; nusxa uchun `a[:]`.

## Odatiy xatolar

- **Indeks chegaradan tashqarida.** `mevalar[3]` (3 ta elementli ro'yxatda) — `IndexError`. Oxirgi indeks: `len(mevalar) - 1` yoki `-1`.
- **`b = a` ni nusxa deb o'ylash.** Ikkala nom bitta ro'yxatga ishora qiladi: `b` ni o'zgartirsangiz, `a` ham o'zgaradi. Nusxa uchun `b = a[:]`.
- **Yo'q elementni `remove` bilan o'chirish.** `ValueError`. Avval `if element in royxat:` bilan tekshiring.
- **`remove` hamma takrorni o'chiradi deb o'ylash.** U faqat birinchisini o'chiradi.
- **`pop` yoki `del` ga qiymat berish.** `bozorlik.pop("banan")` — xato: ular indeks kutadi. Qiymat bo'yicha o'chirish uchun `remove`.
- **`a = a.sort()` yozish.** `sort()` hech narsa qaytarmaydi, shuning uchun `a` ning o'zi `None` bo'lib qoladi. To'g'risi: `a.sort()` yoki `a = sorted(a)`.
- **Funksiya ichida berilgan ro'yxatni tasodifan o'zgartirish.** `royxat.sort()` yoki `royxat.append(...)` tashqaridagi ro'yxatni o'zgartiradi. Nusxa oling: `nusxa = sorted(royxat)` yoki `nusxa = royxat[:]`.
- **Kortejni o'zgartirmoqchi bo'lish.** `koordinata[0] = 0` — `TypeError`. Kortej o'zgarmaydi.
- **To'plamdan indeks bilan olish.** `shaharlar[0]` — `TypeError`: to'plamda tartib yo'q.
- **Bo'sh to'plamni `{}` bilan yaratish.** `{}` to'plam emas. Bo'sh to'plam: `set()`.
