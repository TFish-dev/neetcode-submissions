class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        
        for i in range(len(strs)):
            sublist = []
            freq = {}
            sublist.append(strs[i])
            for char in strs[i]:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            for j in range(len(strs)):
                if j == i:
                    continue
                freqCompare = {}                
                for char in strs[j]:
                    if char in freqCompare:
                        freqCompare[char] += 1
                    else:
                        freqCompare[char] = 1
                
                
                if freq == freqCompare and sublist == []:
                    sublist.append(strs[j])
                    sublist.append(strs[i])

                elif freq == freqCompare:
                    sublist.append(strs[j])

            anagrams.append(sublist)
            
        for i in range(len(anagrams)):
            anagrams[i] = sorted(anagrams[i])

        tupleAnagrams = [tuple(x) for x in anagrams]
        anagrams = list(set(tupleAnagrams))
        anagrams = [list(x) for x in anagrams]
            
        return anagrams