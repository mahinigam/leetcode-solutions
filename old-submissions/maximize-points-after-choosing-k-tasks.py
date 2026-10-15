class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        total = sum(technique2)

        gains = [technique1[i] - technique2[i] for i in range(n)]
        gains.sort(reverse=True)

        for i in range(k):
            total += gains[i]

        for i in range(k, n):
            if gains[i] > 0:
                total += gains[i]
            else:
                break

        return total