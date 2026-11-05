# 2. Operatsion tizimlar va Windows muhitida ishlash

I bob. Kompyuter savodxonligi va arxitekturasi · 1 ta nazariy dars

Ma'ruza taqdimoti: [Zamonaviy kompyuterlar va Windows (PDF)](../../downloads/axv/topic-02/kompyuterlar-va-windows.pdf)

Bu sahifa darsdan keyin takrorlash uchun. Taqdimot ikki mavzuni birga o'z ichiga oladi. Kompyuter turlari va qismlari (CPU, RAM, SSD, kiritish va chiqarish qurilmalari) [1-mavzu sahifasida](topic-01.md) tushuntirilgan. Bu sahifada esa taqdimotning ikkinchi qismi: operatsion tizim, Windows muhiti, oynalar, sozlamalar va dasturlarni o'rnatish.

## Operatsion tizim

### Operatsion tizim nima

Kompyuterda uch tomon bor: siz (foydalanuvchi), dasturlar va qurilmalar (protsessor, xotira, ekran, klaviatura). Ular bir-biri bilan to'g'ridan-to'g'ri gaplashmaydi.

**Operatsion tizim** (*Operating System*, qisqacha **OS**) — foydalanuvchi, dasturlar va kompyuter qurilmalari o'rtasidagi vositachi.

```text
Foydalanuvchi  ↔  Dasturlar  ↔  Operatsion tizim  ↔  Qurilmalar
```

Masalan, siz Word'da hujjatni chop etish tugmasini bosasiz. Word printer bilan o'zi gaplashmaydi: u buni operatsion tizimga aytadi, operatsion tizim esa printerga yuboradi.

Kompyuter yoqilganda birinchi bo'lib operatsion tizim ishga tushadi. Qolgan hamma dasturlar uning ichida ishlaydi.

### Operatsion tizimning vazifalari

| Vazifa | Nima qiladi |
|---|---|
| Qurilmalarni boshqarish | klaviatura, sichqoncha, ekran, printer bilan ishlaydi |
| Fayllarni boshqarish | fayllarni xotirada saqlaydi, topadi va ochadi |
| Dasturlarni ishga tushirish | dasturni ochadi va unga protsessor hamda RAM'dan joy beradi |
| Foydalanuvchilarni boshqarish | bitta kompyuterda har kimning o'z akkaunti va fayllari bo'ladi |
| Xavfsizlikni ta'minlash | parol so'raydi, begona odamni va zararli dasturlarni to'sadi |

**Akkaunt** — kompyuter yoki saytdagi shaxsiy hisobingiz: ismingiz, parolingiz va sozlamalaringiz.

### Operatsion tizim turlari

| Operatsion tizim | Qayerda ishlaydi |
|---|---|
| Windows | ko'pchilik kompyuter va noutbuklar |
| Linux | serverlar va ba'zi kompyuterlar |
| macOS | Apple kompyuterlari (MacBook, iMac) |
| Android | ko'pchilik smartfon va planshetlar |
| iOS | Apple telefonlari (iPhone) |

Telefon ham kompyuter, shuning uchun unda ham operatsion tizim bor. Biz darslarda Windows bilan ishlaymiz.

**Savol.** Windows nima: A) CPU, B) SSD, C) Operatsion tizim?

**Javob.** C) Operatsion tizim. CPU buyruqlarni bajaradigan qurilma, SSD esa ma'lumotni saqlaydigan qurilma. Windows esa qurilma emas, dastur: u qurilmalarni boshqaradi.

## Windows muhiti

### Windows ish stolining asosiy elementlari

Windows yoqilganda ko'radigan birinchi ekraningiz — ish stoli. Unda beshta asosiy element bor:

| Element | Nima |
|---|---|
| Desktop (ish stoli) | butun ekran; unda dastur va fayllarning belgilari (ikonkalari) turadi |
| Taskbar (vazifalar paneli) | ekranning pastidagi uzun chiziq; ochiq dasturlar shu yerda ko'rinadi |
| Start | Taskbar'dagi Windows belgisi; bossangiz Start menyusi ochiladi |
| Search (qidiruv) | dastur, fayl yoki sozlamani nomi bo'yicha topadi |
| Notification Area (bildirishnomalar joyi) | Taskbar'ning o'ng burchagi: soat, Wi-Fi, ovoz, batareya va xabarlar |

**Ikonka** — dastur yoki faylni bildiruvchi kichik rasm. Uni ikki marta bossangiz, dastur yoki fayl ochiladi.

### Start menyusi

Start tugmasini bossangiz, Start menyusi ochiladi. U orqali:

- **dasturlarni ochasiz:** ro'yxatdan dasturni tanlab bosasiz;
- **qidirasiz:** menyu ochilgach dastur nomini yoza boshlasangiz, Windows uni topib beradi;
- **Settings'ga (sozlamalarga) kirasiz:** tishli g'ildirak belgisi;
- **kompyuterni o'chirasiz yoki qayta yoqasiz:** quvvat (⏻) belgisi.

**Shut down** kompyuterni butunlay o'chiradi. **Restart** uni o'chirib, darhol qayta yoqadi. Kompyuter qotib qolsa yoki yangilanishdan keyin Restart so'rasa, shu kerak bo'ladi.

## Oynalar va sozlamalar

### Oyna tugmalari

Har bir dastur o'z **oynasida** ochiladi. Oynaning o'ng yuqori burchagida uchta tugma bor:

| Tugma | Nomi | Nima qiladi |
|---|---|---|
| `_` | Minimize (yig'ish) | oynani yashiradi; dastur Taskbar'da qoladi va ishlashda davom etadi |
| `☐` | Maximize (kattalashtirish) | oyna butun ekranni egallaydi; yana bossangiz, avvalgi o'lchamiga qaytadi |
| `✕` | Close (yopish) | oynani yopadi va dasturni to'xtatadi |

Yig'ilgan oynani qaytarish uchun Taskbar'dagi dastur belgisini bosing.

**Savol.** Siz Word'da yozyapsiz va brauzerga o'tmoqchisiz. Word'dagi ishingiz yo'qolmasligi uchun qaysi tugmani bosasiz: Minimize yoki Close?

**Javob.** Minimize. U oynani faqat yashiradi, Word esa ochiq qoladi. Close esa dasturni yopadi; ishingiz saqlanmagan bo'lsa, Word avval saqlashni so'raydi.

### Settings (sozlamalar)

**Settings** — Windows'ning sozlamalar oynasi. Uni Start menyusidan ochasiz. Asosiy bo'limlar:

| Bo'lim | Nima sozlanadi |
|---|---|
| Wi-Fi | simsiz internet tarmog'iga ulanish |
| Bluetooth | simsiz quloqchin, sichqoncha yoki telefonni ulash |
| Display (ekran) | ekran yorug'ligi va undagi narsalarning o'lchami |
| Sound (ovoz) | ovoz balandligi, karnay va mikrofon |
| Accounts (akkauntlar) | foydalanuvchilar, parol va kirish usuli |
| Apps (dasturlar) | o'rnatilgan dasturlar ro'yxati |
| Windows Update (yangilanish) | Windows'ning yangi versiyalari va xavfsizlik tuzatishlari |

Windows Update'ni o'chirmang: yangilanishlar xatolarni tuzatadi va kompyuterni xavfsizroq qiladi.

### Dastur o'rnatish va o'chirish

**Dastur o'rnatish** — dasturni kompyuterga yozib, ishlashga tayyorlash. Odatda dastur saytidan o'rnatuvchi fayl yuklab olinadi va u ishga tushiriladi.

**Dasturni o'chirish** quyidagi yo'l bilan qilinadi:

```text
Settings  →  Apps  →  Installed apps
```

Ro'yxatdan dasturni topasiz, yonidagi uch nuqta (`…`) tugmasini bosasiz va **Uninstall** (o'chirish) ni tanlaysiz. Ish stolidagi ikonkani o'chirish dasturni o'chirmaydi: dastur kompyuterda qoladi.

Dasturlarni faqat ishonchli manbalardan yuklang: dasturning rasmiy saytidan yoki Microsoft Store'dan. Notanish saytlardagi "bepul" dasturlar ichida zararli dastur bo'lishi mumkin. Bu haqda [6-mavzuda](topic-06.md) batafsil gaplashamiz.

## Odatiy xatolar

- **"Windows — bu kompyuterning qismi."** Windows qurilma emas, operatsion tizim: qurilmalarni boshqaradigan dastur.
- **"Telefonda operatsion tizim yo'q."** Telefon ham kompyuter. Unda Android yoki iOS ishlaydi.
- **Minimize va Close'ni adashtirish.** Minimize oynani yashiradi, dastur ishlayveradi. Close dasturni yopadi.
- **Ikonkani o'chirib, dasturni o'chirdim deb o'ylash.** Dastur Settings → Apps → Installed apps orqali o'chiriladi.
- **Dasturni notanish saytdan yuklash.** Faqat rasmiy sayt yoki Microsoft Store'dan yuklang.
