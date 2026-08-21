class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        # I overcomplicated it and attempted an iterative approach with a new arr of k elements initialized to float('-inf') and some edge case tracking
        if len(self.nums) > 1:
            self.nums.sort()
        
        if len(self.nums) > self.k:
            return self.nums[-self.k]
        else:
            # return None does not pass the test cases
            return self.nums[-self.k]

        # for num in self.nums:
        #     if num > largest:
        #         largest = num
        #     elif num > secondLargest:
        #         secondLargest = num
        # print(self.nums)
        # return secondLargest
