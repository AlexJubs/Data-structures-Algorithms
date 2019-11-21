class Solution:
    def frequencySort(self, s: str) -> str:
        freq =  dict()
        for x in s:
            if freq.get(x) == None: freq[x] = 0
            freq[x] = freq[x] + 1
        freq = sorted(freq.items(), key=operator.itemgetter(1))
        res = ''
        for x in freq:
            res = (x[0])*x[1] + res
        return res