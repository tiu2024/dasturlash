# 4-hafta. Kotlin tilida sinflar va obyektlar

Ma'ruza taqdimoti: [Sinflar va obyektlar (PPTX)](../../../downloads/mobil-ilovalar/week-04/sinflar-va-obyektlar.pptx)

Bu haftaning amaliy qismi: [amaliyot](practice.md).

## Muammo: 500 ta chipta

Konsert ilovasida 500 ta chipta bor. Har biri uchun nom va narxni alohida o'zgaruvchida saqlash mumkin:

```kotlin
val event1 = "Navruz konserti"
val price1 = 150000
val event2 = "Rok kechasi"
val price2 = 90000
// ... yana 498 ta chipta
```

Bu yo'l tez chalkashadi: dastur `event1` bilan `price1` bitta chiptaga tegishli ekanini bilmaydi. Yechim: chiptaning o'zini bitta narsa qilish. Kotlin'da bunday narsa **obyekt** deyiladi.

## Sinf va obyekt

### Sinf — obyekt yasash uchun qolip

Pechenye qolipi bitta, pechenyelar esa ko'p. Dasturda ham shunday:

- **sinf** — qolip: chipta qanday bo'lishini tasvirlaydi;
- **obyekt** — qolipdan yasalgan haqiqiy chipta;
- **xossa** — obyektda saqlanadigan qiymat, masalan nom va narx;
- **konstruktor** — obyektni yasaydigan chaqiruv.

### Obyekt yaratish

Sinf nomini funksiya kabi chaqirsak, yangi obyekt yaratiladi. Xossaga nuqta orqali murojaat qilinadi:

```kotlin
class Ticket(val event: String, var price: Int)

fun main() {
    val first = Ticket("Navruz konserti", 150000)
    val second = Ticket("Rok kechasi", 90000)
    println(first.event)
    println(second.price)
}
```

```text
Navruz konserti
90000
```

Birinchi qator butun sinfni e'lon qiladi. `Ticket(...)` ikkita alohida obyekt yaratadi: har birining o'z nomi va narxi bor. Kotlin'da `new` so'zi yozilmaydi.

**SAVOL.** Qaysi yozuv `Ticket` obyektini yaratadi?

- A. `new Ticket("Rok kechasi", 90000)`
- B. `Ticket("Rok kechasi", 90000)`
- C. `Ticket.create("Rok kechasi", 90000)`
- D. `Ticket = ("Rok kechasi", 90000)`

**JAVOB.** B. Kotlin'da `new` kerak emas: sinf nomi va qavs obyekt yaratadi.

### Asosiy konstruktor

Asosiy konstruktor sinf sarlavhasida, sinf nomidan keyin qavs ichida yoziladi:

- `class Ticket` — yangi sinf va uning nomi;
- `(...)` — asosiy konstruktor: obyekt uchun kerakli qiymatlar;
- `val event` — o'zgarmaydigan xossa;
- `var price` — keyin o'zgartirsa bo'ladigan xossa;
- `: String` — qiymat turi, o'zgaruvchidagidek.

### val va var

`var` xossani o'zgartirish mumkin, `val` xossani esa mumkin emas:

```kotlin
class Ticket(val event: String, var price: Int)

fun main() {
    val t = Ticket("Navruz konserti", 150000)
    t.price = 120000
    println(t.price)
    // t.event = "Boshqa"   // xato: val o'zgarmaydi
}
```

```text
120000
```

Narx o'zgarishi mumkin (chegirma e'lon qilindi), konsert nomi esa o'zgarmasligi kerak. Izohdagi qatorni ochsangiz, Kotlin `Val cannot be reassigned` xatosini beradi.

### Oddiy parametr xossa emas

**SAVOL.** Bu kod nimani chiqaradi?

```kotlin
class Ticket(val event: String, price: Int) {
    val label = "$event: $price so'm"
}

fun main() {
    val t = Ticket("Rok kechasi", 90000)
    println(t.label)
    println(t.price)
}
```

- A. Ikki qator chiqadi
- B. Birinchi qator chiqadi, ikkinchisida xato
- C. Dastur ishga tushmaydi: kompilyatsiya xatosi
- D. Ikkinchi qatorda 0 chiqadi

**JAVOB.** C. `price` oldida `val` ham, `var` ham yo'q, shuning uchun u xossa emas, oddiy parametr: u faqat sinf ichida ishlaydi. `t.price` esa sinf tashqarisida yozilgan, shuning uchun Kotlin `Unresolved reference` xatosini beradi. **Kompilyatsiya xatosi** — dastur ishga tushishidan oldin Kotlin topgan xato: dastur umuman ishlamaydi.

Parametr tashqaridan ko'rinishi uchun uning oldiga `val` yoki `var` yozing.

### Sinf ichidagi funksiya

Sinf ichida funksiya ham yozish mumkin. U obyektning o'z xossalari bilan ishlaydi:

```kotlin
class Ticket(val event: String, var price: Int) {
    fun describe(): String = "$event: $price so'm"
}

fun main() {
    val t = Ticket("Navruz konserti", 150000)
    println(t.describe())
}
```

```text
Navruz konserti: 150000 so'm
```

Funksiya nuqta orqali chaqiriladi: `t.describe()`. Narx o'zgarsa, xuddi shu chaqiruv yangi natija beradi, chunki funksiya obyektning hozirgi holatini o'qiydi.

## Standart qiymat va init

### Standart qiymat

Konstruktor parametriga standart qiymat berish mumkin. Argument berilmasa, shu qiymat ishlatiladi:

```kotlin
class Ticket(val event: String, var price: Int = 100000)

fun main() {
    val a = Ticket("Ochiq dars")
    val b = Ticket("Rok kechasi", 90000)
    println(a.price)
    println(b.price)
}
```

```text
100000
90000
```

`a` uchun narx berilmadi, shuning uchun 100000 ishlatildi. `b` uchun 90000 berildi va u standart qiymatni almashtirdi.

### init blok

Oddiy qiymat berish uchun sarlavha yetadi. Murakkabroq ishlar uchun `init` blok bor: u obyekt yaratilganda o'zi ishga tushadi.

```kotlin
class Ticket(val event: String, var price: Int) {
    init { println("Chipta yaratildi: $event") }
}

fun main() {
    Ticket("Navruz konserti", 150000)
    println("Tayyor")
}
```

```text
Chipta yaratildi: Navruz konserti
Tayyor
```

Biz `init` ni alohida chaqirmadik, shuning uchun "Chipta yaratildi" "Tayyor" dan oldin chiqdi. Sinfda bir nechta `init` bo'lsa, ular yozilgan tartibda ishlaydi.

### require bilan tekshirish

`require` shartni tekshiradi. Shart `False` bo'lsa, xato chiqadi va dastur to'xtaydi. Qavs ichida shart, jingalak qavs ichida xato xabari yoziladi:

```kotlin
class Ticket(val event: String, var price: Int) {
    init {
        require(price >= 0) { "Narx manfiy" }
        println("Chipta yaratildi: $event")
    }
}
```

`init` ichida `require` yozsak, noto'g'ri qiymatli obyekt hech qachon yaratilmaydi: manfiy narxli chipta dasturda paydo bo'lmaydi.

**SAVOL.** Bu kod nimani chiqaradi?

```kotlin
class Ticket(val event: String, var price: Int) {
    init { require(price >= 0) { "Narx manfiy" } }
}
fun main() {
    Ticket("Rok kechasi", 90000)
    println("1-chipta tayyor")
    Ticket("Xato chipta", -5)
    println("2-chipta tayyor")
}
```

**JAVOB.** `1-chipta tayyor` chiqadi, keyin `IllegalArgumentException` xatosi chiqadi va dastur to'xtaydi. Ikkinchi chiptada shart `False` (`-5 >= 0` noto'g'ri), shuning uchun oxirgi qatorga dastur yetib bormaydi. Kotlin `-5` ni dastur ishga tushishidan oldin tekshirmaydi: bu faqat dastur ishlayotganda aniqlanadi.

## Ikkilamchi konstruktor va companion object

### Ikkilamchi konstruktor

Ilovada narxni foydalanuvchi matn maydoniga yozadi, ya'ni qiymat `String` bo'lib keladi. **Ikkilamchi konstruktor** obyektni boshqa qiymat turi bilan yaratishga imkon beradi. U sinf ichida `constructor` so'zi bilan yoziladi:

```kotlin
class Ticket(val event: String, var price: Int) {
    constructor(event: String, text: String) :
        this(event, text.toIntOrNull() ?: 0)
}

fun main() {
    println(Ticket("Rok", "85000").price)
    println(Ticket("Rok", "abc").price)
}
```

```text
85000
0
```

`toIntOrNull()` matn son bo'lsa, sonni; bo'lmasa `null` beradi. `?:` belgisi `null` o'rniga 0 qo'yadi. Shuning uchun `"abc"` kelsa ham dastur sinmaydi.

### Avval asosiy konstruktor ishlaydi

Ikkilamchi konstruktor har doim avval asosiy konstruktorga murojaat qilishi kerak. Buni `: this(...)` qiladi:

- `: this(...)` asosiy konstruktorni chaqiradi;
- avval asosiy konstruktor va `init` ishlaydi;
- keyin ikkilamchi konstruktorning tanasi ishlaydi.

**SAVOL.** Bu kod nimani chiqaradi?

```kotlin
class Ticket(val event: String, var price: Int) {
    init { println("init") }
    constructor(event: String) : this(event, 0) {
        println("ikkilamchi")
    }
}
fun main() {
    Ticket("Ochiq dars")
}
```

**JAVOB.** Avval `init`, keyin `ikkilamchi` chiqadi. Ikkilamchi konstruktor birinchi `this(event, 0)` orqali asosiy konstruktorni (va `init` ni) ishga tushiradi, shundan keyingina o'z tanasini bajaradi.

### Companion object

`companion object` ichidagi funksiyani chaqirish uchun obyekt kerak emas: u sinf nomi bilan chaqiriladi.

```kotlin
class Ticket(val event: String, var price: Int) {
    companion object {
        fun free(event: String) = Ticket(event, 0)
    }
}

fun main() {
    val ticket = Ticket.free("Ochiq dars")
    println(ticket.event)
    println(ticket.price)
}
```

```text
Ochiq dars
0
```

Bu sinfning o'ziga tegishli ishlar uchun qulay, masalan tayyor chipta yasovchi funksiya.

## Odatiy xatolar

- **`new` yozish.** `new Ticket(...)` — Kotlin'da bunday yozuv yo'q. To'g'risi: `Ticket(...)`.
- **Parametrga `val` yoki `var` yozmaslik.** Keyin `t.price` ishlamaydi. Parametr tashqaridan ko'rinishi uchun `val` yoki `var` yozing.
- **`val` xossani o'zgartirish.** `t.event = "Boshqa"` xato beradi. O'zgaradigan qiymat uchun `var` ishlating.
- **`require` xatoni to'xtatmaydi deb o'ylash.** Shart `False` bo'lsa, dastur to'xtaydi va keyingi qatorlar bajarilmaydi.
- **Ikkilamchi konstruktorda `: this(...)` ni unutish.** Ikkilamchi konstruktor har doim asosiy konstruktorga murojaat qilishi kerak.
