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
