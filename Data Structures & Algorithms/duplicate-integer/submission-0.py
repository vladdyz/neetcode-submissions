class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = {}
        for num in nums:
            if num in mySet:
                return True
            else:
                mySet[num] = 1
        return False