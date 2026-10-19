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
