class Ticket(val event: String, var price: Int)

fun main() {
    val first = Ticket("Navruz konserti", 150000)
    val second = Ticket("Rok kechasi", 90000)
    println("${first.event}: ${first.price} so'm")
    println("${second.event}: ${second.price} so'm")
}
