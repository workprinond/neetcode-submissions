class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = []
        for w1,w2 in zip(word1,word2):
            result.append(w1 + w2)
           

        if len(word1) > len(word2):
            result.append(word1[len(word2):])
        else:
            result.append(word2[len(word1):])
        return ''.join(result)