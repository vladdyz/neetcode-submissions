class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1:
        #     return -1

        # I tried to get fancy here and recursively call the search function with a sliced version of the nums array, and also wrap it in a try...except block to return the -1 if nothing was found
        # it did not work lol
        low = 0
        high = len(nums) -1 # ALWAYS -1 because this is INCLUSIVE and will result in out of bounds
        #mid = len(nums) // 2
        while high >= low:
            # this can cause integer overflow in some programming languages (e.g. C++)
            # but its fine for Python...
            # in C++ it would be:mid = low + (high - low) // 2
            mid = (low + high) // 2
            if nums[mid] > target:
                #newNums = nums[0:mid]
                #return self.search(newNums, target)
                high = mid - 1
            elif nums[mid] < target:
                #newNums = nums[mid+1:]
                #return self.search(newNums, target)
                low = mid + 1
            else:
                return mid # NOT nums[mid] which is the VALUE at the index
        return -1