# Amaliyot

Bu sahifada [ma'ruzada](lecture.md) o'rganilgan sinflar va obyektlar bo'yicha chipta (`Ticket`) misolida 8 ta masala keltirilgan. Har bir masala shartidan keyin **Yechim** bloki joylashgan: u yopiq turadi, ustiga bosib oching. Avval masalani o'zingiz yechib ko'ring va natijani namuna bilan solishtiring, keyin yechim va tushuntirishni o'qing.

Har bir yechim ichida shu dasturning `.kt` fayliga havola bor. Kodni [Kotlin Playground](https://play.kotlinlang.org/) da ishga tushirib ko'rishingiz mumkin.

## 1. Ikkita chipta

**Masala.** Ikkita `Ticket` obyektini yarating: "Navruz konserti" (150000 so'm) va "Rok kechasi" (90000 so'm). Har bir chiptani alohida qatorda `nom: narx so'm` ko'rinishida chiqaring.

Namuna:

```text
Navruz konserti: 150000 so'm
Rok kechasi: 90000 so'm
```

??? success "Yechim"

    ```kotlin
    class Ticket(val event: String, var price: Int)

    fun main() {
        val first = Ticket("Navruz konserti", 150000)
        val second = Ticket("Rok kechasi", 90000)
        println("${first.event}: ${first.price} so'm")
        println("${second.event}: ${second.price} so'm")
    }
    ```

    Fayl: [p1.kt](../../../downloads/mobil-ilovalar/week-04/p1.kt)

    **Tushuntirish.**

    - `class Ticket(val event: String, var price: Int)` — asosiy konstruktor ikkita xossani e'lon qiladi ([ma'ruzada](lecture.md#asosiy-konstruktor)).
    - `Ticket(...)` ikkita alohida obyekt yaratadi; `new` yozilmaydi ([ma'ruzada](lecture.md#obyekt-yaratish)).
    - Satr ichida oddiy o'zgaruvchi `$event` kabi yoziladi. Nuqtali yozuv (`first.event`) esa `{ }` ichiga olinadi: `${first.event}`. Aks holda Kotlin faqat `first` ni oladi.

## 2. Narx o'zgarishi

**Masala.** `Ticket` sinfiga `describe()` funksiyasini qo'shing: u `nom: narx so'm` satrini qaytarsin. "Navruz konserti" chiptasini 150000 so'm bilan yarating va chiqaring. Keyin narxni 120000 so'mga tushiring va yana chiqaring.

Namuna:

```text
Navruz konserti: 150000 so'm
Navruz konserti: 120000 so'm
```

??? success "Yechim"

    ```kotlin
    class Ticket(val event: String, var price: Int) {
        fun describe(): String = "$event: $price so'm"
    }

    fun main() {
        val ticket = Ticket("Navruz konserti", 150000)
        println(ticket.describe())
        ticket.price = 120000
        println(ticket.describe())
    }
    ```

    Fayl: [p2.kt](../../../downloads/mobil-ilovalar/week-04/p2.kt)

    **Tushuntirish.**

    - `describe()` sinf ichida yozilgan, shuning uchun `event` va `price` ni to'g'ridan-to'g'ri ishlatadi ([ma'ruzada](lecture.md#sinf-ichidagi-funksiya)).
    - `price` xossasi `var`, shuning uchun uni o'zgartirish mumkin. `event` esa `val`: `ticket.event = "Boshqa"` yozsangiz, xato chiqadi ([ma'ruzada](lecture.md#val-va-var)).
    - Narx o'zgargach, xuddi shu `describe()` chaqiruvi yangi narxni chiqaradi.

## 3. Standart narx

**Masala.** `Ticket` sinfida narx berilmasa, 100000 so'm bo'lsin. "Ochiq dars" chiptasini narxsiz, "Rok kechasi" chiptasini 90000 so'm bilan yarating va ikkalasini `describe()` bilan chiqaring.

Namuna:

```text
Ochiq dars: 100000 so'm
Rok kechasi: 90000 so'm
```

??? success "Yechim"

    ```kotlin
    class Ticket(val event: String, var price: Int = 100000) {
        fun describe(): String = "$event: $price so'm"
    }

    fun main() {
        val lesson = Ticket("Ochiq dars")
        val rock = Ticket("Rok kechasi", 90000)
        println(lesson.describe())
        println(rock.describe())
    }
    ```

    Fayl: [p3.kt](../../../downloads/mobil-ilovalar/week-04/p3.kt)

    **Tushuntirish.**

    - `price: Int = 100000` — standart qiymat. Argument berilmasa, shu qiymat ishlatiladi ([ma'ruzada](lecture.md#standart-qiymat)).
    - "Rok kechasi" uchun 90000 berilgan, u standart qiymatni almashtiradi.

## 4. Narxni tekshirish

**Masala.** `Ticket` obyekti yaratilganda `Chipta yaratildi: <nom>` qatori chiqsin. Narx manfiy bo'lsa, obyekt yaratilmasin va dastur xato bilan to'xtasin. Ikkita to'g'ri chipta yarating va oxirida `Ikkala chipta tayyor` ni chiqaring.

Namuna:

```text
Chipta yaratildi: Navruz konserti
Chipta yaratildi: Rok kechasi
Ikkala chipta tayyor
```

Ikkinchi chiptaning narxini `-5` ga almashtirsangiz:

```text
Chipta yaratildi: Navruz konserti
Exception in thread "main" java.lang.IllegalArgumentException: Narx manfiy
```

(Kotlin Playground bu xato qatoridan keyin yana bir necha texnik qator ko'rsatadi.)

??? success "Yechim"

    ```kotlin
    class Ticket(val event: String, var price: Int) {
        init {
            require(price >= 0) { "Narx manfiy" }
            println("Chipta yaratildi: $event")
        }
    }

    fun main() {
        Ticket("Navruz konserti", 150000)
        Ticket("Rok kechasi", 90000)
        println("Ikkala chipta tayyor")
    }
    ```

    Fayl: [p4.kt](../../../downloads/mobil-ilovalar/week-04/p4.kt)

    **Tushuntirish.**

    - `init` blok har bir obyekt yaratilganda o'zi ishga tushadi ([ma'ruzada](lecture.md#init-blok)).
    - `require(shart) { xabar }` shart `False` bo'lsa, `IllegalArgumentException` xatosini beradi va dastur to'xtaydi ([ma'ruzada](lecture.md#require-bilan-tekshirish)). `require` tekshiruvi `println` dan oldin turibdi, shuning uchun noto'g'ri chiptada "Chipta yaratildi" chiqmaydi.
    - Ikkinchi namunada birinchi chipta to'g'ri, shuning uchun uning qatori chiqadi. Xato ikkinchisida chiqadi va `Ikkala chipta tayyor` qatoriga dastur yetib bormaydi.
    - `-5` ni Kotlin dastur ishga tushishidan oldin tekshirmaydi: xato faqat dastur ishlayotganda aniqlanadi.

## 5. Chegirmali narx

**Masala.** `Ticket` sinfiga `withDiscount(percent: Int)` funksiyasini qo'shing: u narxdan `percent` foizni ayirib, yangi narxni qaytarsin (chiptaning o'z narxi o'zgarmaydi). Foiz 0 dan 100 gacha (0 va 100 ham kiradi) bo'lmasa, xato chiqsin. 150000 so'mlik chiptaga 20, 0 va 100 foiz chegirmani hisoblang.

Namuna:

```text
120000
150000
0
```

??? success "Yechim"

    ```kotlin
    class Ticket(val event: String, var price: Int) {
        fun withDiscount(percent: Int): Int {
            require(percent in 0..100) { "Foiz 0 dan 100 gacha bo'lishi kerak" }
            return price - price * percent / 100
        }
    }

    fun main() {
        val ticket = Ticket("Navruz konserti", 150000)
        println(ticket.withDiscount(20))
        println(ticket.withDiscount(0))
        println(ticket.withDiscount(100))
    }
    ```

    Fayl: [p5.kt](../../../downloads/mobil-ilovalar/week-04/p5.kt)

    **Tushuntirish.**

    - Chegirma summasi `price * percent / 100`: 150000 va 20 foiz uchun 30000. Uni narxdan ayiramiz: 120000.
    - `0..100` — 0 dan 100 gacha sonlar oralig'i, ikkala chegara ham kiradi. `percent in 0..100` foiz shu oraliqda ekanini tekshiradi.
    - Funksiya `price` ni o'zgartirmaydi, faqat yangi narxni qaytaradi, shuning uchun uchala chaqiruv ham 150000 dan hisoblanadi.
    - Bu yerda `/` butun sonlarni bo'ladi va kasr qismini tashlab yuboradi (masalan, `7 / 2` — 3).

## 6. Matn ko'rinishidagi narx

**Masala.** Ilovada narx matn maydonidan `String` bo'lib keladi. `Ticket` sinfiga ikkilamchi konstruktor qo'shing: u narxni matn sifatida olsin. Matn son bo'lmasa, narx 0 bo'lsin. "Navruz konserti" uchun `"85000"`, "Rok kechasi" uchun `"abc"` ni sinab ko'ring.

Namuna:

```text
Navruz konserti: 85000 so'm
Rok kechasi: 0 so'm
```

??? success "Yechim"

    ```kotlin
    class Ticket(val event: String, var price: Int) {
        constructor(event: String, text: String) :
            this(event, text.toIntOrNull() ?: 0)
    }

    fun main() {
        val a = Ticket("Navruz konserti", "85000")
        val b = Ticket("Rok kechasi", "abc")
        println("${a.event}: ${a.price} so'm")
        println("${b.event}: ${b.price} so'm")
    }
    ```

    Fayl: [p6.kt](../../../downloads/mobil-ilovalar/week-04/p6.kt)

    **Tushuntirish.**

    - Ikkilamchi konstruktor `constructor(...)` bilan yoziladi va `: this(...)` orqali avval asosiy konstruktorni chaqiradi ([ma'ruzada](lecture.md#ikkilamchi-konstruktor)).
    - Kotlin ikkala konstruktorni argument turiga qarab ajratadi: `Int` bo'lsa asosiy, `String` bo'lsa ikkilamchi ishlaydi.
    - `text.toIntOrNull()` matn son bo'lsa, sonni; bo'lmasa `null` beradi. `?: 0` esa `null` o'rniga 0 qo'yadi.

## 7. Bepul chipta

**Masala.** `Ticket` sinfiga `free(event)` funksiyasini qo'shing: u berilgan tadbir uchun narxi 0 bo'lgan chipta qaytarsin. Funksiya obyekt yaratmasdan, sinf nomi bilan chaqirilsin. "Ochiq dars" uchun bepul chipta yarating va chiqaring.

Namuna:

```text
Ochiq dars: 0 so'm
```

??? success "Yechim"

    ```kotlin
    class Ticket(val event: String, var price: Int) {
        companion object {
            fun free(event: String) = Ticket(event, 0)
        }
    }

    fun main() {
        val ticket = Ticket.free("Ochiq dars")
        println("${ticket.event}: ${ticket.price} so'm")
    }
    ```

    Fayl: [p7.kt](../../../downloads/mobil-ilovalar/week-04/p7.kt)

    **Tushuntirish.**

    - `companion object` ichidagi funksiya sinf nomi bilan chaqiriladi: `Ticket.free(...)`. Buning uchun oldindan obyekt kerak emas ([ma'ruzada](lecture.md#companion-object)).
    - `fun free(event: String) = Ticket(event, 0)` — qisqa yozuv: funksiya `=` dan keyingi qiymatni qaytaradi.

## 8. Chiptalar ro'yxati

**Masala.** Uchta chiptadan ro'yxat tuzing: "Navruz konserti" (150000), "Rok kechasi" (90000) va "Ochiq dars" (0). Har bir chiptani `nom: narx so'm` ko'rinishida chiqaring, oxirida jami narxni `Jami: ... so'm` qatorida ko'rsating.

Namuna:

```text
Navruz konserti: 150000 so'm
Rok kechasi: 90000 so'm
Ochiq dars: 0 so'm
Jami: 240000 so'm
```

??? success "Yechim"

    ```kotlin
    class Ticket(val event: String, var price: Int)

    fun main() {
        val tickets = listOf(
            Ticket("Navruz konserti", 150000),
            Ticket("Rok kechasi", 90000),
            Ticket("Ochiq dars", 0)
        )
        var total = 0
        for (ticket in tickets) {
            println("${ticket.event}: ${ticket.price} so'm")
            total += ticket.price
        }
        println("Jami: $total so'm")
    }
    ```

    Fayl: [p8.kt](../../../downloads/mobil-ilovalar/week-04/p8.kt)

    **Tushuntirish.**

    - Obyektlarni o'tgan haftadagi kolleksiyalarda ham saqlash mumkin: `listOf(...)` ro'yxati `Ticket` obyektlaridan iborat.
    - `for (ticket in tickets)` ro'yxatdagi har bir chiptani birma-bir oladi.
    - `total` har aylanishda joriy chiptaning narxini oladi: 0 + 150000 + 90000 + 0 = 240000.

## Qisqa lug'at

| Atama | Ma'nosi |
|---|---|
| `class` | yangi sinf (qolip) e'lon qiladi |
| obyekt | sinfdan yaratilgan haqiqiy qiymat |
| xossa | obyektda saqlanadigan qiymat |
| `val` / `var` | o'zgarmaydigan / o'zgaradigan xossa |
| `init` | obyekt yaratilganda ishlaydigan blok |
| `require` | shart `False` bo'lsa, xato chiqaradi |
| `constructor` | ikkilamchi konstruktor |
| `companion object` | sinf nomi bilan chaqiriladigan funksiyalar joyi |
| `toIntOrNull()` | matnni songa aylantiradi, bo'lmasa `null` beradi |
| `${...}` | satr ichiga ifoda joylaydi |
