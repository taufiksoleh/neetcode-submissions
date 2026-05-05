class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in have:
                return [have[diff], i]
            have[n] = i
        