# 1-hafta. Dasturlashga kirish

Ma'ruza taqdimoti: [Dasturlashga kirish (PPTX)](../../../downloads/dasturlash/week-01/dasturlash-ga-kirish.pptx)

## Kompyuter fani — muammolarni hal qilish

Kompyuter fanining mohiyati — **muammoni hal qilish**. Muammo kirish ma'lumoti sifatida beriladi, uni hal qiluvchi **algoritm** "qora quti" vazifasini bajaradi, natija esa chiqish ma'lumoti bo'ladi.

```text
kirish  →  algoritm  →  chiqish
```

Masalan, telefon daftarida ismni topish: kirish — ism va daftar, chiqish — telefon raqami.

Sun'iy intellekt vositalari ko'p ishni osonlashtiradi, lekin asoslarni bilmasdan turib, ular bergan kodni tushunish, tekshirish va tuzatish mumkin emas. Shuning uchun biz asoslardan boshlaymiz.

## Sonlar: birlik va ikkilik sanoq tizimi

Hisoblashning eng sodda usuli — **birlik (unary)** tizimi: har bir birlik uchun bitta barmoq ko'tariladi. Bu usulda faqat 10 gacha sanash mumkin.

Kompyuterlar **ikkilik (binary)** tizimidan foydalanadi. U faqat ikkita raqamga ega: `0` va `1`. Har bir raqam **bit** (*binary digit*) deyiladi. Kompyuter ichidagi tranzistorlarni yoqilgan yoki o'chirilgan lampochkalar deb tasavvur qilish mumkin: o'chiq — `0`, yoniq — `1`.

Odatdagi o'nlik sonda raqamlar o'rni 1, 10, 100 kabi 10 ning darajalarini bildiradi. Ikkilik sonda esa o'rinlar 2 ning darajalarini bildiradi: ..., 4, 2, 1.

Uchta lampochka bilan 0 dan 7 gacha sanash mumkin:

| O'nlik | 4 | 2 | 1 | Ikkilik |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | `000` |
| 1 | 0 | 0 | 1 | `001` |
| 2 | 0 | 1 | 0 | `010` |
| 3 | 0 | 1 | 1 | `011` |
| 4 | 1 | 0 | 0 | `100` |
| 5 | 1 | 0 | 1 | `101` |
| 6 | 1 | 1 | 0 | `110` |
| 7 | 1 | 1 | 1 | `111` |

Sakkizta bit **bayt** (*byte*) deb ataladi. Bayt o'rinlari: 128, 64, 32, 16, 8, 4, 2, 1. Shuning uchun bitta bayt 0 dan 255 gacha sonni saqlaydi:

- `00000101` = 4 + 1 = 5
- `11111111` = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255

Python bu o'zgartirishlarni bajarishga imkon beradi:

```python
n = 5
print(format(n, "08b"))    # sonni 8 bitli ikkilik matnga aylantiradi
print(int("00000101", 2))  # ikkilik matnni songa aylantiradi
print(int("11111111", 2))
```

Kutilgan natija:

```text
00000101
5
255
```

## Matn: ASCII va Unicode

Kompyuter faqat sonlarni saqlaydi, shuning uchun har bir harfga alohida son tayinlangan. Bu kelishuv **ASCII** (*American Standard Code for Information Interchange*) deb ataladi. Masalan, bosh `A` harfi — `65`, ya'ni ikkilikda `01000001`. ASCII jadvali 128 ta belgini (0–127) o'z ichiga oladi.

Aytaylik, telefonga `72 73 33` sonlari kelgan. ASCII bo'yicha bu `H`, `I`, `!`, ya'ni "HI!" matni:

```python
for kod in [72, 73, 33]:
    print(kod, chr(kod))

print(ord("A"))
```

Kutilgan natija:

```text
72 H
73 I
33 !
65
```

`chr(son)` son bo'yicha belgini, `ord(belgi)` esa belgi bo'yicha sonni qaytaradi.

ASCII faqat ingliz alifbosi uchun yetarli. O'zbek, rus, xitoy tillaridagi harflar va boshqa belgilar uchun **Unicode** standarti yaratilgan. U ASCII'dagi belgilarni saqlaydi va ularga boshqa ko'plab belgilarni, jumladan emojilarni qo'shadi. Emoji ham aslida son; har bir qurilma ishlab chiqaruvchisi uni o'zicha chizadi, shuning uchun u turli telefonlarda biroz farq qiladi.

```python
print(ord("😀"))
print(chr(128512))
```

Kutilgan natija:

```text
128512
😀
```

## Rang, rasm, video va musiqa

Rang odatda **RGB** (*Red, Green, Blue*) usulida beriladi: qizil, yashil va ko'k tuslarning har biri uchun bir bayt, ya'ni 0 dan 255 gacha son. Demak, bitta nuqta (**piksel**) uchun uchta bayt kerak.

Yuqoridagi `72, 73, 33` sonlari matn emas, rang sifatida talqin qilinsa, to'q zaytun (sarg'ish-yashil) tusni bildiradi. Ma'lumotning ma'nosini uni qanday talqin qilishimiz belgilaydi.

Python'da rangni qavs ichidagi uchta son bilan yozish mumkin: qizil, yashil, ko'k.

```python
rang = (72, 73, 33)
oq = (255, 255, 255)
qora = (0, 0, 0)
print(rang, oq, qora)
```

Kutilgan natija:

```text
(72, 73, 33) (255, 255, 255) (0, 0, 0)
```

- **Rasm** — piksellar to'plami, har bir piksel uchta son.
- **Video** — ketma-ket almashadigan ko'plab rasmlar.
- **Musiqa** — tovush to'lqinining har bir lahzadagi balandligini bildiruvchi sonlar ketma-ketligi (yoki notalar uchun: balandligi, davomiyligi va kuchi).

Demak, kompyuterdagi hamma narsa — sonlar, sonlar esa — bitlar.

## Algoritmlar

**Algoritm** — masalani hal qilishning aniq, bosqichma-bosqich ko'rsatmalari.

Telefon daftarida ismni topishning uchta usulini ko'rib chiqamiz. Daftarda n ta sahifa bor deylik.

1. **Sahifama-sahifa** ko'rish. Eng yomon holatda n ta sahifani ko'rishga to'g'ri keladi.
2. **Ikkitalab** ko'rish. Eng yomon holatda taxminan n/2 ta sahifa.
3. **Daftarni o'rtasidan ochish**: ism o'rtadan oldin bo'lsa, chap yarmini, aks holda o'ng yarmini qoldiramiz va jarayonni takrorlaymiz. Har qadamda ish ikki barobar kamayadi, shuning uchun qadamlar soni taxminan log₂ n.

Uchinchi usul **ikkilik qidiruv** (*binary search*) deyiladi. 1000 sahifali daftar uchun birinchi usulda 1000 qadam, uchinchisida atigi 10 qadam yetadi. Algoritm samaradorligi shunday baholanadi: kirish hajmi kattalashganda qadamlar soni qanchalik tez o'sadi. Buning uchun **O-katta (Big-O)** belgilash ishlatiladi. Unda o'zgarmas ko'paytuvchilar tashlab yuboriladi, chunki muhimi — o'sish tezligi. Shuning uchun birinchi usul O(n), ikkinchisi taxminan n/2 qadam bo'lsa ham baribir O(n), uchinchisi esa O(log n).

## Psevdokod

**Psevdokod** — algoritmni odam tushunadigan tilda yozish usuli. U kod yozishdan oldin mantiqni aniqlashtiradi va boshqalarga niyatimizni tushuntirishga yordam beradi.

Telefon daftarida ikkilik qidiruv:

```text
1  Daftarni qo'lga oling
2  Daftarni o'rtasidan oching
3  Agar ko'rib chiqiladigan sahifa qolmagan bo'lsa
4      Ish tugadi: ism daftarda yo'q
5  Sahifaga qarang
6  Agar ism sahifada bo'lsa
7      Qo'ng'iroq qiling va ishni tugating
8  Aks holda agar ism shu sahifadan oldin bo'lsa
9      Daftarning chap yarmining o'rtasini oching
10     3-qatorga qayting
11 Aks holda
12     Daftarning o'ng yarmining o'rtasini oching
13     3-qatorga qayting
```

Ism sahifada bo'lmasa, u yo shu sahifadan oldin, yo keyin bo'ladi. Shuning uchun oxirgi "aks holda" — "ism shu sahifadan keyin" degani. To'xtash sharti esa 3-qatorda: qidiriladigan sahifa qolmasa, ism daftarda yo'q.

Bu yerda dasturlashning qurilish bloklari allaqachon ko'rinib turibdi:

- **Funksiyalar** — bajariladigan harakatlar (fe'llar): "qo'lga oling", "oching", "qarang", "qo'ng'iroq qiling".
- **Shartlar** — "agar … aks holda agar … aks holda" yo'llari. Shart **mantiqiy ifoda**ga, ya'ni javobi "ha" yoki "yo'q" bo'lgan savolga tayanadi: "sahifa qoldimi?", "ism sahifada bormi?", "ism shu sahifadan oldinmi?". Python'da "ha" `True` (to'g'ri), "yo'q" esa `False` (noto'g'ri) deb yoziladi.
- **Takrorlash (sikl)** — "3-qatorga qayting".

To'rtinchi blok — **o'zgaruvchi**: qiymatni nom ostida saqlash joyi. Psevdokodda u yo'q edi, lekin Python'da ko'p ishlatiladi.

## Psevdokoddan Python kodiga

Xuddi shu g'oyani Python'da yozamiz. Daftar o'rniga tartiblangan ismlar ro'yxatidan foydalanamiz:

```python
def ikkilik_qidiruv(ismlar, ism):
    chap = 0
    ong = len(ismlar) - 1
    while chap <= ong:
        orta = (chap + ong) // 2
        if ismlar[orta] == ism:
            return orta
        elif ism < ismlar[orta]:
            ong = orta - 1
        else:
            chap = orta + 1
    return -1


daftar = ["Ali", "Bobur", "Dilnoza", "Eldor", "Zilola"]
print(ikkilik_qidiruv(daftar, "Eldor"))
print(ikkilik_qidiruv(daftar, "Sardor"))
```

Kutilgan natija:

```text
3
-1
```

Natija topilgan ismning o'rnini (0 dan boshlab) beradi; `-1` ism topilmaganini bildiradi.

Kodda to'rt blokning hammasi bor:

- `ikkilik_qidiruv`, `len`, `print` — **funksiyalar**;
- `if` / `elif` / `else` — **shartlar**; `chap <= ong`, `ismlar[orta] == ism`, `ism < ismlar[orta]` — mantiqiy ifodalar (`True` yoki `False` beradi);
- `while` — **takrorlash**;
- `chap`, `ong`, `orta` — **o'zgaruvchilar**.

Ro'yxat **tartiblangan** bo'lishi shart: aks holda "o'rtadan oldin yoki keyin" degan mulohaza ma'noga ega bo'lmaydi.

Bu dasturni hozircha to'liq tushunmasangiz, xavotir olmang: funksiyalar, shartlar va sikllarni keyingi haftalarda batafsil o'rganamiz. Asosiysi — psevdokod va kod orasidagi o'xshashlikni ko'rish.

## Abstraksiya

Murakkab ishni boshqarish uchun uni qismlarga bo'lamiz va har bir qismni nom bilan atab, ichki tafsilotlarini unutamiz. Bunga **abstraksiya** deyiladi. Biz `print` yozganimizda ekranga piksellar qanday chizilishini bilishimiz shart emas. Dasturlash tillari ham shunday paydo bo'lgan: ikkilik kodni yozish juda og'ir, shuning uchun inson tushunadigan tillar yaratilgan va ular boshqalarning ishi ustiga quriladi.

## Odatiy xatolar

- **Ikkilik sonni o'qishda o'rinlarni adashtirish.** O'ngdagi raqam eng kichik o'rin (1), chapga qarab 2, 4, 8 ... Masalan, `100` — to'rt, bir yuz emas.
- **`A` va `a` ni bir xil deb o'ylash.** ASCII'da `A` = 65, `a` = 97.
- **Raqam belgisi bilan sonni adashtirish.** `"5"` belgi (ASCII 53), `5` esa son.
- **Ikkilik qidiruvni tartiblanmagan ro'yxatda qo'llash.** Natija noto'g'ri chiqadi.
- **Psevdokodda "3-qatorga qayting" ni unutish.** Takrorlashsiz algoritm faqat bir marta ishlaydi.
- **To'xtash shartini unutish.** Ism daftarda bo'lmasa, "sahifa qolmadi" sharti bo'lmagan algoritm hech qachon tugamaydi.
