class Solution:
    def scoreBalance(self, s: str) -> bool:
        scores = [ord(c) - ord('a') + 1 for c in s]
        total = sum(scores)

        left_sum = 0

        for i in range(len(s) - 1):
            left_sum += scores[i]
            right_sum = total - left_sum
            if left_sum == right_sum: 
                return True
        return False