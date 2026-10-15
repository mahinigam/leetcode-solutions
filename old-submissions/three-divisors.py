class Solution:
    def isThree(self, n: int) -> bool:
        root = int(n ** 0.5)

        if root * root != n:
            return False

        for i in range(2, int(root ** 0.5) + 1):
            if root % i == 0:
                return False

        return root > 1