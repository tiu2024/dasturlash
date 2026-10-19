class Ticket(val event: String, var price: Int) {
    companion object {
        fun free(event: String) = Ticket(event, 0)
    }
}

fun main() {
    val ticket = Ticket.free("Ochiq dars")
    println("${ticket.event}: ${ticket.price} so'm")
}
