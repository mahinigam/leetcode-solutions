class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        digits = '0123456789'

        allowed = vowels + consonants + digits

        if len(word) < 3:
            return False

        has_vowels = False
        has_consonants = False

        for c in word:
            if c.lower() in vowels: has_vowels = True
            if c.lower() in consonants: has_consonants = True

            if c.lower() not in allowed: return False

        return has_vowels and has_consonants
