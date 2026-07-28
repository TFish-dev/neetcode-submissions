class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convertToChar(word):
            charCount = [0] * 26
            
            for char in word:
                key = ord(char) - ord('a')
                charCount[key] += 1
                
            return charCount
        
        wordCountDict = {}
        
        for word in strs:
            wordCharCount = tuple(convertToChar(word))
        
            if wordCharCount in wordCountDict:
                wordCountDict[wordCharCount].append(word)
                
            else:
                wordCountDict[wordCharCount] = [word]
            
        out = []
        
        for k, v in wordCountDict.items():
            out.append(v)
            
        return out