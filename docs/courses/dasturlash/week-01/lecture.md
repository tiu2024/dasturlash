# 1-hafta. Dasturlashga kirish

Ma'ruza taqdimoti: [Dasturlashga kirish (PPTX)](../../../downloads/dasturlash/week-01/dasturlash-ga-kirish.pptx)

## Dasturlash 1, 2 — bu Computer Science

Bu kurs **Computer Science** (kompyuter fanlari) asoslaridan boshlanadi. Computer Science — muammolarni, ularni yechish jarayonini va shu jarayondan kelib chiqadigan yechimlarni o'rganadigan fan.

### Keng tarqalgan noto'g'ri tushunchalar

| Noto'g'ri tushuncha | Aslida |
|---|---|
| "Computer Science = dasturlash" | Dasturlash — biz ishlatadigan vosita, fanning o'zi emas. |
| "Computer Science = matematika" | Matematika — asos, lekin maqsad emas. |
| "Juda aqlli bo'lish kerak" | Sabrli, qiziquvchan va tizimli bo'lish kerak. |
| "Bu kompyuterlar haqida" | Bu muammolar haqida; kompyuter shunchaki vosita. |

## Computational thinking

**Computational thinking** (hisoblash tafakkuri) — kompyuter olimlarining muammoga yondashish usuli. U to'rtta ustunga tayanadi.

### 1. Dekompozitsiya

Murakkab muammoni kichikroq, boshqarish osonroq qismlarga bo'lish.

Misol — veb-sayt yaratish. Bu katta ishni bir nechta kichik ishga bo'lish mumkin:

- dizayn va sahifalar tartibini loyihalash;
- ma'lumotlar bazasini qurish (sayt ma'lumotlari saqlanadigan joy);
- server mantig'ini yozish (saytning ko'rinmaydigan, orqada ishlaydigan qismi);
- foydalanuvchi hisoblari va xavfsizlikni ta'minlash.

### 2. Naqsh aniqlash

Yangi muammo bilan avval yechilgan muammolar orasidagi o'xshashlikni sezish.

Misol — saralash. Guruh ro'yxatini ism bo'yicha, reyting jadvalini ball bo'yicha, qidiruv natijalarini moslik bo'yicha tartiblash — bularning hammasi aslida bitta muammo: narsalarni tartibga solish. Bitta yaxshi saralash usulini o'rgansangiz, uni hamma joyda ishlata olasiz.

### 3. Abstraksiya

Hozir muhim bo'lmagan tafsilotlarni chetga qo'yib, muhim narsaga e'tibor qaratish.

Misol — "Saqlash" tugmasi. Uni bosganda kompyuter faylni diskka qanday yozishini, xotirani qanday boshqarishini bilishingiz shart emas. Bu murakkab ish baribir bajariladi, lekin u bitta oddiy tugma ortida yashiringan.

### 4. Algoritm yaratish

**Algoritm** — muammoni yechimga aylantiradigan aniq, tartiblangan qadamlar.

Misol — taom retsepti. Unda aniq qadamlar aniq tartibda yozilgan; har safar unga amal qilinsa, bir xil natija chiqadi.

### To'rt ustun birgalikda: eng yuqori ball

60 ta talabaning imtihon ballari ro'yxatda berilgan, ro'yxat tartiblanmagan. Eng yuqori ballni topish kerak.

- **Dekompozitsiya.** 60 ta ballni bir vaqtda solishtirmang — ularni birma-bir ko'rib chiqing.
- **Naqsh aniqlash.** Bu "eng yaxshisini top" masalasi — xuddi sport musobaqasida g'olibni aniqlash kabi.
- **Abstraksiya.** Ballar qanday yig'ilgani yoki qayerda saqlangani muhim emas — faqat ularni solishtira olish kerak.
- **Algoritm:**

```text
1. Birinchi ballni "hozircha eng kattasi" deb belgilang.
2. Keyingi ballni "hozircha eng kattasi" bilan solishtiring.
3. Agar u kattaroq bo'lsa, endi "hozircha eng kattasi" — shu ball.
4. Ballar tugamagan bo'lsa, 2-qadamga qayting.
5. "Hozircha eng kattasi" — javob.
```

Birinchi ball hech narsa bilan solishtirilmaydi, qolgan 59 tasi bittadan solishtiriladi. Natija: aniq 59 ta solishtirish va har doim to'g'ri javob.

## Muammolarni yechish

### Asosiy model: kirish → algoritm → chiqish

```text
kirish  →  algoritm  →  chiqish
```

- **Kirish** — bizga berilgan narsa: boshlang'ich ma'lumot.
- **Algoritm** — kirishni chiqishga aylantiradigan aniq qadamlar.
- **Chiqish** — javob: muammo nimani so'ragan bo'lsa, o'sha.

Eng yuqori ball masalasida kirish — 60 ta ball, chiqish — ularning eng kattasi.

### Yaxshi algoritm qanday bo'ladi?

- **To'g'ri** — har qanday to'g'ri kirish uchun har doim to'g'ri javob beradi.
- **Samarali** — vaqt va boshqa resurslarni behuda sarflamaydi.
- **Tushunarli** — boshqa odam (yoki kelajakdagi siz) uni o'qib, unga ishona oladi.

### Bitta muammo, ikki xil algoritm

Muammo: 1000 betlik lug'atdan bitta so'zni topish.

| | Yondashuv | Qancha ish |
|---|---|---|
| Yomon | 1-betdan boshlab, so'zni topguncha betlarni birma-bir varaqlash | o'rtacha ~500 marta varaqlash |
| Yaxshi | Lug'atni o'rtasidan ochish. So'z shu betdan oldinmi yoki keyinmi — o'sha yarmini olib, yana o'rtasidan ochish | ~10 marta ochish |

Ikkinchi usulda har ochishda qidiriladigan betlar ikki baravar kamayadi: 1000 → 500 → 250 → … → 1. Shuning uchun 10 ga yaqin qadam yetadi. Bu usul lug'atdagi so'zlar alifbo tartibida bo'lgani uchun ishlaydi. Ikkala algoritm ham to'g'ri, lekin ikkinchisi ancha samarali.

## Ma'lumotni ifodalash

### Hammasi kalitdan boshlanadi

Kompyuterning asosiy qurilish bloki — **tranzistor**. Uni juda kichik elektr kaliti deb tasavvur qiling: u faqat ikki holatda bo'ladi — **yoniq** yoki **o'chiq**. Yoniq holat `1`, o'chiq holat `0` bilan belgilanadi.

Kompyuterdagi har qanday ma'lumot — matn, rasm, tovush, video — oxir-oqibat shu ikki holatdan tuzilgan naqshlardir.

### Unar — eng oddiy tizim

**Unar** tizimda son bitta belgini shuncha marta takrorlab yoziladi. Barmoq bilan sanash ham shunday:

```text
3  →  ● ● ●
7  →  ● ● ● ● ● ● ●
```

Muammo: 1000 sonini yozish uchun 1000 ta belgi kerak. Sonlar kattalashgani sari bu usul juda noqulay bo'lib qoladi.

### Ikkilik tizim

**Ikkilik** (*binary*) tizim faqat ikki raqamdan foydalanadi: `0` va `1`. Har bir shunday raqam **bit** deyiladi.

| O'nlik son | Ikkilik yozuvi |
|:---:|:---:|
| 0 | `0` |
| 1 | `1` |
| 2 | `10` |
| 3 | `11` |
| 4 | `100` |
| 5 | `101` |
| 6 | `110` |
| 7 | `111` |

Har bir qatorda chapda — tanish o'nlik son, o'ngda — xuddi shu sonning ikkilik yozuvi. Ikkalasi bir xil miqdorni bildiradi, faqat yozilishi boshqacha.

### O'rin qiymati

O'nlik tizimda o'rinlar 1, 10, 100 … bo'lgani kabi, ikkilik tizimda o'rinlar har safar ikki baravar oshadi: 1, 2, 4, 8, 16, 32, 64, 128. Sonni o'qish uchun `1` turgan o'rinlarning qiymatlari qo'shiladi:

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |

```text
00101101  =  32 + 8 + 4 + 1  =  45
```

O'nlik tizimda ham xuddi shu g'oya, faqat 2 ta emas, 10 ta raqam (0–9) bilan. O'nlik tizim, ehtimol, odamlarning 10 ta barmog'i bo'lgani uchun paydo bo'lgan:

| 100 | 10 | 1 |
|:---:|:---:|:---:|
| 0 | 4 | 5 |

```text
045  =  (0 × 100) + (4 × 10) + (5 × 1)  =  45
```

Sakkizta bit **bayt** deyiladi. Bir baytga eng kichigi `00000000` = 0, eng kattasi `11111111` = 255 sig'adi.

### Matn: ASCII

Kompyuter faqat sonlarni tushunsa, `A` harfini qanday saqlaydi? Javob oddiy: har bir belgiga kelishuv asosida bitta son beriladi. Bu kelishuv **ASCII** deb ataladi.

| Belgi | O'nlik | Ikkilik (8 bit) |
|:---:|:---:|:---:|
| `A` | 65 | `01000001` |
| `a` | 97 | `01100001` |
| `0` | 48 | `00110000` |
| `!` | 33 | `00100001` |

Katta `A` va kichik `a` — har xil sonlar. Raqam belgisi `0` ham nol soni emas, balki belgi: uning kodi 48.

ASCII atigi 128 ta belgini qamrab oladi. Ingliz tili uchun bu yetarli, lekin dunyoning boshqa tillari uchun emas.

### Matn: Unicode

**Unicode** xuddi shu g'oyani 149 000 dan ortiq belgiga kengaytiradi: deyarli barcha tillarning harflari, turli belgilar va emojilar. Har bir belgining Unicode'dagi raqami `U+` dan keyin yoziladi:

| Belgi | Unicode |
|:---:|:---:|
| A | `U+0041` |
| é | `U+00E9` |
| 中 | `U+4E2D` |
| م | `U+0645` |
| 😀 | `U+1F600` |

Asosiy g'oya ASCII bilan bir xil — har bir belgi uchun bitta son, faqat jadval ancha katta. Bu sonlarni xotirada tejamkor saqlash usuli **UTF-8** deb ataladi.

### Rang: RGB

Ekrandagi har bir rang qizil (**R**ed), yashil (**G**reen) va ko'k (**B**lue) yorug'likni aralashtirib hosil qilinadi. Har bir rangning ulushi 0 dan 255 gacha son bilan beriladi, ya'ni bitta bayt.

| R, G, B | Rang |
|---|---|
| 255, 0, 0 | qizil |
| 0, 200, 0 | yashil |
| 0, 0, 255 | ko'k |
| 0, 0, 0 | qora |
| 255, 255, 255 | oq |

Demak, bitta rang — uchta son. `(255, 0, 0)` kompyuterda uchta 8 bitli ikkilik son sifatida saqlanadi — xuddi ASCII kodlari kabi.

### Hammasi — bitlar

```text
matn    →  sonlar         (ASCII / Unicode)
rang    →  sonlar         (RGB)
sonlar  →  ikkilik tizim  (0 va 1)
0 va 1  →  elektr         (yoniq / o'chiq)
```

## CSE dan keyingi kasblar

**CSE** (*Computer Science and Engineering*) — kompyuter fanlari va muhandisligi. Bitta mutaxassislik ko'p yo'nalishlarga yo'l ochadi:

| Yo'nalish | Nima qilinadi |
|---|---|
| Dasturiy ta'minot muhandisligi | odamlar har kuni ishlatadigan ilovalar va tizimlarni qurish |
| Data Science va ML | ma'lumotlardagi bog'liqliklarni topish, bashorat qiluvchi va sun'iy intellekt modellarini qurish (ML — *machine learning*, mashinali o'qitish) |
| Kiberxavfsizlik | tizimlar, ma'lumotlar va odamlarni raqamli tahdidlardan himoya qilish |
| Mahsulot menejmenti | texnik jamoa bilan biznes va foydalanuvchilar ehtiyojlari o'rtasida ko'prik bo'lish |
| Tadqiqot | hisoblash imkoniyatlari chegaralarini kengaytirish |
| Embedded systems | atrofimizdagi jismoniy qurilmalarni (maishiy texnika, avtomobil, sensorlar) dasturlash |

- 15 yil oldin "full-stack dasturchi" (saytning ham ko'rinadigan, ham orqa qismini yozadigan dasturchi) degan lavozim deyarli yo'q edi. Kasblar o'zgarib turadi.
- Ko'p zamonaviy rollar bir nechta ko'nikmani birlashtiradi: masalan, ma'lumotlar bilan ishlaydigan muhandis yoki kod ham yozadigan xavfsizlik mutaxassisi.
- Eng katta boylik lavozim nomi emas, balki shu ma'ruzadagi asosiy fikrlash ko'nikmalari.
- Tadbirkorlik ham haqiqiy yo'l: CSE bitiruvchilari o'z mahsulotlarini yaratadi.

## Dasturlashda sun'iy intellekt

Sun'iy intellekt (AI) — dasturchining yangi vositasi:

- **Kod yozish** — AI yordamchilari tavsif bo'yicha kod yozib beradi.
- **Xatolarni tuzatish** — xato xabarlarini tushuntiradi va yechim taklif qiladi.
- **O'rganish** — notanish kod yoki tushunchani so'rasangiz, tushuntirib beradi.

Lekin bu baribir vosita, tushunish o'rnini bosmaydi. Muammoni to'g'ri qo'yish va natijani baholash — insonning ishi.

AI davrida quyidagi ko'nikmalar kamroq emas, aksincha ko'proq kerak:

- **Computational thinking** — AI dan yechim so'rashdan yoki uni baholashdan oldin muammoni qismlarga bo'lish kerak.
- **Baholash qobiliyati** — AI yozgan kod ishonchli ko'rinsa ham noto'g'ri bo'lishi mumkin; buni sezish uchun yetarlicha bilim kerak.
- **Muammoni aniq qo'yish** — "chiqindi kirsa, chiqindi chiqadi": noaniq so'rovga noaniq javob keladi.
- **Asoslar** — bugun o'rgangan ma'lumotni ifodalash g'oyalari AI yaratgan hamma narsaning ostida yotadi.

AI bilan qanday ishlash haqida: [Sun'iy intellektdan foydalanish](../ai-guide.md).

## Odatiy xatolar

- **Ikkilik sonni chapdan o'qish.** O'rin qiymatlari o'ngdan boshlanadi: 1, 2, 4, 8 … Masalan, `100` — to'rt, yuz emas.
- **`A` va `a` ni bir xil deb o'ylash.** ASCII'da `A` = 65, `a` = 97.
- **Raqam belgisini son deb o'ylash.** `0` belgisining kodi 48; u nol soni emas, belgi.
- **"Dasturlash = Computer Science" deb o'ylash.** Dasturlash — vosita; asosiy ish — muammoni tushunish va yechish.
- **Algoritmda qadamni tushirib qoldirish.** Masalan, eng yuqori ball algoritmida "2-qadamga qayting" bo'lmasa, faqat ikkita ball solishtiriladi.
- **AI javobini tekshirmasdan qabul qilish.** AI ishonchli ohangda ham xato javob berishi mumkin.
