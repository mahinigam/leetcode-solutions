class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter(s1.split()) + Counter(s2.split())

        ans = []

        for word in c:
            if c[word] == 1:
                ans.append(word)

        return ans