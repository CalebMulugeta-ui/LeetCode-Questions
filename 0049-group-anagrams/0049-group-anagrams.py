class Solution(object):
    from collections import defaultdict

    def groupAnagrams(self, strs) :

        anagramMap = defaultdict(list)
        res = []



        for w in strs:
            sortedWord = sorted(w)
            sorted_string = "".join(sortedWord) 
            if sorted_string in anagramMap:
                anagramMap[sorted_string].append(w)
            else:
                anagramMap[sorted_string].append(w)

        for keys in anagramMap.values():
            res.append(keys)
        
        return res
