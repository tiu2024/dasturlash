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
