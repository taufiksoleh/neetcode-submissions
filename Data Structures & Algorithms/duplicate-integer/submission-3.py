class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        v = set()
        for i in range(len(nums)):
            if nums[i] in v:
                return True
            v.add(nums[i])
        return False