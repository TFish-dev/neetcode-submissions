class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = {}
        letters2 = {}

        for v in s:
            if v not in letters1:
                letters1[v] = 1
            else:
                letters1[v] += 1

        for v in t:
            if v not in letters2:
                letters2[v] = 1
            else:
                letters2[v] += 1

        if letters1 == letters2:
            return True
        else:
            return False

        

        