class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s): return s.count(min(s))
        words = sorted(list(map(f, words)))
        queries = list(map(f, queries))
        res = list()
        for x in queries:
            temp = 0
            if x >= words[-1]:
                res.append(0)
                continue
            if x < words[0]:
                res.append(len(words))
                continue
            p = len(words)-1
            temp = 0
            while (x < words[p]) and p >= 0:
                p = p-1
                temp = temp+1
            res.append(temp)
        return res
