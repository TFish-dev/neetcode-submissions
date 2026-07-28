import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        translator = str.maketrans('', '', string.punctuation)
        cleanText = s.translate(translator)

        if cleanText[::-1] == cleanText:
            return True
        else:
            return False