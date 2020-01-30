class Solution:
    def countCharacters(self, words, chars):
        S1 = {        'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0
        }
        for x in chars: S1[x] = S1[x] +1
        S2 = dict(S1)
        inc = True
        res = 0
        for word in words:
            for char in word: 
                if S1[char] > 0:
                    inc = True
                    S1[char] = S1[char] - 1
                else: 
                    inc = False
                    break
            if inc:
                res = res+len(word)
            S1 = dict(S2)

        return res