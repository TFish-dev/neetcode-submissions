class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = set()

        for i in range(len(nums)):
            previous_length = len(items)
            items.add(nums[i])
            if previous_length == len(items):
                return True

        return False