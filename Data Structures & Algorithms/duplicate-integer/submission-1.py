class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(sorted(set(nums))) != len(sorted(nums))
    
        