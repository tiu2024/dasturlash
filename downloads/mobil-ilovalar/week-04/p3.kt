class Ticket(val event: String, var price: Int = 100000) {
    fun describe(): String = "$event: $price so'm"
}

fun main() {
    val lesson = Ticket("Ochiq dars")
    val rock = Ticket("Rok kechasi", 90000)
    println(lesson.describe())
    println(rock.describe())
}
