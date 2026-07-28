class Solution:
    def trap(self, height: List[int]) -> int:
        already_counted = []
        total_water = 0

        for i in range(len(height)):
            if height[i] == 0 or i in already_counted:
                continue
            
            pillar_height = height[i]
            ending_index = None
            
            for j in range(i + 1, len(height)):
                if height[j] >= pillar_height:
                    ending_index = j
                    break
                
            if ending_index is None:
                if i + 1 >= len(height):
                    continue
                
                ending_index = len(height) - 1
                
                for k in range(len(height) - 1, i, -1):
                    if height[k] > height[ending_index]:
                        ending_index = k
                        
            ending_height = height[ending_index]
            water_level = min(pillar_height, ending_height)
            
            water_to_add = 0
            
            for j in range(i + 1, ending_index):
                water_to_add += max(0, water_level-height[j])
                already_counted.append(j)
                
            total_water += water_to_add
                
        return total_water