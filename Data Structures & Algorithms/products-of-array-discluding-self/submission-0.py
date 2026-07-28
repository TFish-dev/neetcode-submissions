class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        removeIndex = 0

        while removeIndex < len(nums):
                number = 1
                for i in range(len(nums)):
                        if i == removeIndex:
                                continue

                        number *= nums[i]
                products.append(number)
                removeIndex += 1
                

        return products