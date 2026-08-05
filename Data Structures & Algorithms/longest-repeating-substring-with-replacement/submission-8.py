class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = {}
        res = 0

        if len(s) == 1:
            return 1

        if k == 0:
            current = s[0]
            longest = 1
            for i in range(1, len(s)):
                if s[i] == current:
                    longest += 1
                else:
                    current = s[i]
                    longest = 1
                res = max(res, longest)
            return res


        for i in range(len(s)):
            if s[i] in charSet:
                charSet[s[i]] += 1
            else:
                charSet[s[i]] = 1

        for c in charSet:
            l = 0
            count = 0
            numReplacements = 0

            for r in range(len(s)):
                count += 1
                
                if c != s[r]:
                    numReplacements += 1
                    
                while numReplacements > k:
                    if s[l] != c:
                        numReplacements -= 1
                    l += 1
                    count -= 1
                
                if count > res:
                    res = count

        return res