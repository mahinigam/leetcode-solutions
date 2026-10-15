class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sl = s.split()
        return len(sl[-1])