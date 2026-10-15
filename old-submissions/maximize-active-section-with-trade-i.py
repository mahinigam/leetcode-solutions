class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        ones = s.count('1')

        blocks = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks.append((s[i], j - i))
            i = j

        max_gain = 0
        for i in range(1, len(blocks) - 1):
            if (
                blocks[i][0] == '1'
                and blocks[i - 1][0] == '0'
                and blocks[i + 1][0] == '0'
            ):
                max_gain = max(
                    max_gain,
                    blocks[i - 1][1] + blocks[i + 1][1]
                )

        return ones + max_gain