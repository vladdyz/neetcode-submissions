class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                # smash!
                stones = stones[:-2]
            #elif stones[-1] > stones[-2]:
            else:
                stones[-1] = stones[-1] - stones[-2]
                stones.pop(-2)
                stones.sort()

        if stones:
            return stones[0]
        else:
            return 0 

        