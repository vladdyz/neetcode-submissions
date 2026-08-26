class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mySet = {} # O(1) Lookup
        for i, num in enumerate(nums):
            # to not overwrite the value if a given number appears more than once in the list, just record the first instance
            if num not in mySet:
                mySet[num] = i
            
        for i, num in enumerate(nums):
            if target - num in mySet and mySet[target-num] != i:
                # neetcode wants this sorted
                return sorted([i, mySet[target-num]])
        return []

        