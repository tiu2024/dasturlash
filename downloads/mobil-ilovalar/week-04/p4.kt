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
