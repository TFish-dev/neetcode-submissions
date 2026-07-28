class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        i = 0
        j = len(heights) - 1

        while i != j:
            waterHeight = (j - i) * min(heights[i], heights[j])
            if waterHeight > maxArea:
                maxArea = waterHeight

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1


        return maxArea