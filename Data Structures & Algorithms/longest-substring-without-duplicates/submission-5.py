class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        if len(s) == 1:
            return 1

        elif len(s) == 2 and s[0] != s[1]:
            return 2
        
        for i in range(len(s)):
            longest = 1
            seen = []
            seen.append(s[i])

            for j in range(i + 1, len(s)):
                if s[j] in seen:
                    break
                else:
                    longest += 1
                    seen.append(s[j])
            
            if longest > result:
                result = longest
                
        return result