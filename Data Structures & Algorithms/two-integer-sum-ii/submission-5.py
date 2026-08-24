class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Straightforward solution: Nested loops to check each index in the array (O(n^2))
        # map out each element with their index
        numMap = {}
        for i in range(len(numbers)):
            if numbers[i] not in numMap: # if there are duplicates, it will overwrite the indices...
                numMap[numbers[i]] = i 
        
        for i, num in enumerate(numbers):
            if target - num in numMap and numMap[target-num] < i:
                # 1-indexes = add 1 to the index (e.g. start at 1, not at 0...)
                return [numMap[target-num] + 1, i + 1]
        return 0
        
        