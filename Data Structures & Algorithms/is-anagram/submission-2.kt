class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if (s.length != t.length) return false
        val sortedS = s.toList().sorted()
        val sortedT = t.toList().sorted()
        return sortedS == sortedT
    }
}
