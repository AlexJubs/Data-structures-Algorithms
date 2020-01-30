class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        arr = A.split(' ') + B.split(' ')
        hash_s = dict()
        res = []
        for x in arr:
            if hash_s.get(x) is None: hash_s[x] = 0
            hash_s[x] = hash_s[x] + 1
            
        for item in hash_s:
            if hash_s[item] == 1: res.append(item)
        return res