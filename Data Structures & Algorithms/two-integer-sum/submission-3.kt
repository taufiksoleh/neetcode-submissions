class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var setValue = mutableSetOf<Int>()
        for ((k,v) in nums.withIndex()) {
            var min = target - v
            if (setValue.contains(min)) {
                return intArrayOf(nums.indexOf(min), k)
            }
            setValue.add(v)
        }
        return intArrayOf()
    }
}
