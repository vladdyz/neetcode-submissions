class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myNums = {}
        results = []
        for num in nums:
            if num in myNums:
                myNums[num] += 1
            else:
                myNums[num] = 1
        
        for i in range(k):
            highestFreq = 0
            topElement = None
            for num in myNums:
                if myNums[num] > highestFreq:
                    highestFreq = myNums[num]
                    topElement = num
            results.append(topElement)
            myNums.pop(topElement)
        
        return results

        

        