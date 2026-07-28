class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sFrequency = [0] * 26
        tFrequency = [0] * 26
        
        for i in range(len(s)):
            sIndex = ord(s[i]) - ord('a')
            tIndex = ord(t[i]) - ord('a')
            
            sFrequency[sIndex] += 1
            tFrequency[tIndex] += 1
            
        if sFrequency == tFrequency:
            return True
        else:
            return False

        

        