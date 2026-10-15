class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        t = 0

        for i in range(1, n+1):
            if t == len(target):
                break

            if i == target[t]:
                res.append("Push")
                t += 1
            else:
                res.append("Push")
                res.append("Pop")

        return res