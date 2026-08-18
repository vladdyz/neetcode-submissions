class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a map of the nums for O(1) time complexity for look ups
        #mySet = set(nums)
        # the map needs an index where the value is taken from for the return statement and to ensure the same index is not being used for both values

        mySet = {}
        for i, num in enumerate(nums):
            # to not overwrite the value if a given number appears more than once in the list, just record the first instance
            if num not in mySet:
                mySet[num] = i
            
        # I always struggle on the second loop
        # primarily with remembering the mySet[target-num] and not comparing an index to a value
        for i, num in enumerate(nums):
            if target - num in mySet and mySet[target-num] != i:
                #return [i, mySet[target-num]]
                # neetcode wants this sorted
                return sorted([i, mySet[target-num]])
        return []

        