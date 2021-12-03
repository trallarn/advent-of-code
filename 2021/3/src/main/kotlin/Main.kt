fun main() {
    val filename = "3-input.csv"
    val lines = ClassLoader.getSystemResourceAsStream(filename).reader().readLines()
        .map { line ->
            line.split("")
                .filter { it.isNotEmpty() }
        }

    part1(lines)
    part2(lines)
}

fun part1(lines: List<List<String>>) {
    val rows = Rows(lines)
    println("Part 1: ${rows.getGamma() * rows.getBeta()}")
}

fun part2(lines: List<List<String>>) {
    val rows = Rows(lines)
    println("Part 2: ${rows.getOxygen() * rows.getC02()}")
}

data class Rows(val rows: List<List<String>>) {
    private val cols = 12
    private val keys = listOf("0", "1")

    fun getOxygen(): Int {
        val matches = getMatches(0, rows, Oxygen())
        return toDecimal(matches)
    }

    fun getC02(): Int {
        val matches = getMatches(0, rows, CO2())
        return toDecimal(matches)
    }

    private fun toDecimal(row: List<String>) =
        Integer.parseInt(row.joinToString(""), 2)

    private fun getMatches(col: Int, filtered: List<List<String>>, type: Type): List<String> {
        if (filtered.size < 2) {
            return filtered[0]
        }
        val mask = getTypeFrequencies(col, filtered)
        val newFiltered = filtered.filter { row -> row[col] == mask.getMatch(type) }
        return getMatches(col + 1, newFiltered, type)
    }

    fun getGamma() =
        (0 until cols)
            .map { getTypeFrequencies(it, rows) }
            .joinToString(separator = "") { it.max() }
            .let { Integer.parseInt(it, 2) }

    fun getBeta() =
        (0 until cols)
            .map { getTypeFrequencies(it, rows) }
            .joinToString(separator = "") { it.min() }
            .let { Integer.parseInt(it, 2) }

    private fun getTypeFrequencies(col: Int, rows: List<List<String>>): TypeFrequencies =
        rows.map { it[col] }
            .groupBy { it }
            .let { group -> TypeFrequencies(keys.map { TypeFrequency.of(it, group) }) }
}

data class TypeFrequencies(val items: List<TypeFrequency>) {
    init {
        require(items.size == 2)
    }

    fun max() = items.maxByOrNull { it.frequency }!!.type
    fun min() = items.minByOrNull { it.frequency }!!.type
    fun getMatch(type: Type): String =
        when(type) {
            is Oxygen -> {
                val extreme = items.maxByOrNull { it.frequency }!!.frequency
                matchOrOnTie(extreme, type.winnerOnTie)
            }
            is CO2 -> {
                val extreme = items.minByOrNull { it.frequency }!!.frequency
                matchOrOnTie(extreme, type.winnerOnTie)
            }
        }

    private fun matchOrOnTie(frequencyNeedle: Int, winnerOnTie: String): String {
        val maxRows = items.filter { it.frequency == frequencyNeedle }
        return if (maxRows.size == 1) {
            maxRows[0].type
        } else {
            winnerOnTie
        }
    }
}

data class TypeFrequency(val type: String, val frequency: Int) {
    companion object {
        fun of(type: String, group: Map<String, List<String>>) =
            TypeFrequency(type, group[type]?.size ?: 0)
    }
}

sealed class Type(val winnerOnTie: String)
class Oxygen: Type(winnerOnTie = "1")
class CO2: Type(winnerOnTie = "0")
