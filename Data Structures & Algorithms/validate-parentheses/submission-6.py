class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        result = []
        opn = ['(', '[', '{']
        cls = [')', ']', '}']

        for i in range(len(s)):
            if s[i] in opn:
                result.append(s[i])

            elif s[i] in cls:
                if not result:
                    return False

                index = cls.index(s[i])
                if result[-1] == opn[index]:
                    result.pop()
                else:
                    return False

        if len(result) > 0:
            return False
        return True