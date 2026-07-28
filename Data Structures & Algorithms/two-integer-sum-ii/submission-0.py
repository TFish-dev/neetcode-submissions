class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i == j:
                    continue
                
                if numbers[i] + numbers[j] == target:
                    out.append(i + 1)
                    out.append(j + 1)

                    return out