class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        val bucket: MutableSet<Int> = mutableSetOf()
        for (n in nums) {
            // chekc dupliation
            if (bucket.contains(n)) {
                return true
            }
            bucket.add(n)
        }
        return false
    }
}
