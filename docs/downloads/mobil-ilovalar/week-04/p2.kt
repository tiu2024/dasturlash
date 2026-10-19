class Ticket(val event: String, var price: Int) {
    fun describe(): String = "$event: $price so'm"
}

fun main() {
    val ticket = Ticket("Navruz konserti", 150000)
    println(ticket.describe())
    ticket.price = 120000
    println(ticket.describe())
}
