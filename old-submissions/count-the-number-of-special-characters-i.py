class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        ls = 'abcdefghijklmnopqrstuvwxyz'

        return sum(1 for ch in ls if ch in s and ch.upper() in s)