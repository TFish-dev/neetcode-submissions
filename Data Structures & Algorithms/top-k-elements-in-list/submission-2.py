class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        count_dict_reversed = {}
        out = []
        for v in nums:
            if v in count_dict:
                count_dict[v] += 1
            else:
                count_dict[v] = 1
                
        for key, value in count_dict.items():
            if value in count_dict_reversed.keys():
                count_dict_reversed[value].append(key)
            else:
                count_dict_reversed[value] = [key]
        print(count_dict)    
        print(count_dict_reversed)        
        
        while len(out) < k:
            max_freq = max(count_dict_reversed)
            vals = count_dict_reversed[max_freq]
            
            for v in vals:
                if len(out) < k:
                    out.append(v)
                    
            count_dict_reversed.pop(max_freq)

        return out