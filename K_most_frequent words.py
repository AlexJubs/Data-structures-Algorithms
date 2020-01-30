"""
sort the elements in alphebetical order
build a hashtable plotting the elements with their frequency
build an output array ordered from the highest frequency in the hashtable to the lowest
pop the output array untill there are k elements
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        HashT = {}
        S = set()
        for x in words:
            if x not in S:
                HashT[x] = 1
                S.add(x)
            else:
                HashT[x] = HashT[x] + 1
        res = []
        for i in range(k):
            m = max(HashT.values())
            for x,y in HashT.items():
                if (y == m):
                    temp = x
                    res.append(x)
                    break
            del HashT[temp]

        return res