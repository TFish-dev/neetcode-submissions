class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateCheck = set()

        for v in nums:
            if v in duplicateCheck:
                return True
            duplicateCheck.add(v)

        return False