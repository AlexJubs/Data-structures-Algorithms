class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = dict(zip(list('abcdefghijklmnopqrstuvwxyz'),[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
        res = set()
        for word in words:
            morse = ''
            for letter in word:
                morse = morse + morse_dict[letter]
            res.add(morse)
        return len(res)
