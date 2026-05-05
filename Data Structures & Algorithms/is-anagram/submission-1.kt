class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        val sortedS = s.toList().sorted()
        val sortedT = t.toList().sorted()
        return sortedS == sortedT
    }
}
