class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # value -> index

        for k, v in enumerate(nums):
            diff = target - v
            if diff in hashMap:
                return [hashMap[diff], k]
            hashMap[v] = k
        return []
