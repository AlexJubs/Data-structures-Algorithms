class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for x in strs:
            if len(res) == 0:
                res.append([x])
            else:
                for i in range(len(res)):
                    if self.anagram(res[i][0],x):
                        res[i].append(x)
                        break
                    if (i == len(res)-1):
                        res.append([x])
        return res
 
    def anagram(self, A: str, B: str)-> bool:
        if (len(A) != len(B)): return False
        HashA, HashB = {},{}

        for x in A:
            if x not in HashA:
                HashA[x] = 1
            if x in HashA:	
                HashA[x] = HashA[x] + 1

        for y in B:
            if y not in HashB:
                HashB[y] = 1
            if y in HashB:	
                HashB[y] = HashB[y] + 1
        return HashA == HashB