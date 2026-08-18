class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        zeroFlag = 0 # this used to be a bool but the actual non-example test cases can contain more than one zero
        for i in range(len(nums)):
            # handle zero cases in the next loop
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeroFlag += 1
                
        for i in range(len(nums)):
            # if an array contains more than a single zero, every single product will inevitably be multiplied by a zero and will result in a 0
            if zeroFlag > 1:
                output.append(0)
            else: 
                if zeroFlag and nums[i] != 0:
                    output.append(0)
                else: 
                    output.append(product)
        for i in range(len(output)):
            if nums[i] != 0:
                output[i] /= nums[i]
            # else:
            #     output[i] 
            # just leave it alone
            output[i] = int(output[i])


        return output

        