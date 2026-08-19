class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for x in count:
            if count[x] > 1:
                return True
        return False
    
        