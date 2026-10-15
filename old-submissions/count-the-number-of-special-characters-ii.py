class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        s = 'abcdefghijklmnopqrstuvwxyz'

        for ch in s:
            if ch in word and ch.upper() in word:
                if word.rindex(ch) < word.index(ch.upper()):
                    ans += 1

        return ans