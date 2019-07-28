"""
We need a helper function to check if 2 strings are anagrams using a hashtable so we can do it in linear time. We then traverse the string s, and check every string of length len(p) starting at s[i]. When we reach the index len(s)-len(p) then we stop. For each time we find an anagram, we add its index to an output array
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hmap = {}  # will remove add into this
        hori = {}   # original map
        for ch in p:
            hmap[ch] = hmap.get(ch, 0) + 1
            hori[ch] = hori.get(ch, 0) + 1

        rs = []
        idx, mv, ln = 0, 0, len(s)
        while mv < ln:
            ch = s[mv]
            if ch in hmap:
                hmap[ch] -= 1
                if hmap[ch] == 0:
                    del hmap[ch]

                if len(hmap) == 0:
                    rs.append(idx)
                mv += 1
            elif ch not in hori:
                mv += 1  # this char doesn't exists in ori
                         # so start from scratch
                idx = mv
                hmap = hori.copy()
            else:
                hmap[s[idx]] = 1
                idx += 1

        return rs