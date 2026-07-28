class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encodedString = ""
        wordLengths = []
        for word in strs:
                wordLengths.append(str(len(word)))
                wordLengths.append(",")

        wordLengths.append("$")

        for i in range(len(wordLengths)):
                encodedString += str(wordLengths[i])

        for v in strs:
                encodedString += str(v)

        return encodedString                                                                                                           

    def decode(self, s: str) -> List[str]:

        numIndex = 0
        wordLengths = ""
        text = ""
        while s[numIndex] != "$":
            wordLengths += s[numIndex]
            numIndex += 1
        wordLengths = wordLengths.split(",")[:-1]
        numIndex += 1


        for char in s[numIndex:]:
            text += char

        decodedList = []
        prev = 0

        for l in wordLengths:
            if l == ",":
                continue

            tempText = ""
            nxt = int(l)
            for char in text[prev:prev + nxt]:
                    tempText += char
            decodedList.append(tempText)
            prev += nxt

        return decodedList