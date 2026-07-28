class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert_char(word):
            char_count_list = [0]*26
            for c in word:
                idx = (ord(c) - ord('a'))
                char_count_list[idx] += 1
            return char_count_list
        
        word_count_dict = {}
        for w in strs:
            char_count = tuple(convert_char(w))
            
            if char_count in word_count_dict:
                word_count_dict[char_count].append(w)
            else:
                word_count_dict[char_count] = [w]
                
        out = []
        
        for k,v in word_count_dict.items():
            out.append(v)
        
        return out