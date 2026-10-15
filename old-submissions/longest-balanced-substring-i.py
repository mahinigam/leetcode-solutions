from collections import Counter

class Solution:
    def longestBalanced(self, s: str) -> int:
        temp = s
        n = len(temp)
        max_len = 0

        for i in range(n):
            freq = Counter()
            for j in range(i, n):
                freq[temp[j]] += 1
                values = list(freq.values())
                if len(set(values)) == 1:
                    max_len = max(max_len, j-i+1)

        return max_len