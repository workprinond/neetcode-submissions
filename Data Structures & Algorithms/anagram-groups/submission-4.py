class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        result = []
        
        for word in strs:
            found = False
            for group in result:
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    found = True
                    break
            
            if not found:
                result.append([word])
        
        return result

        