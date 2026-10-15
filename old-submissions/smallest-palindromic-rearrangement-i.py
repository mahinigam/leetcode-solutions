class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)

        left = []
        mid = ""

        for i in range(26):
            ch = chr(ord('a') + i)
            left.append(ch * (cnt[ch] // 2))
            if cnt[ch] % 2:
                mid = ch

        left = "".join(left)
        return left + mid + left[::-1]