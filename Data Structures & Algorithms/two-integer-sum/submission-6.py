class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # value -> index

        for k, v in enumerate(nums):
            hashMap[v] = k

        for k, v in enumerate(nums):
            diff = target - v
            if diff in hashMap and hashMap[diff] != k:
                return [k, hashMap[diff]]
        return []
