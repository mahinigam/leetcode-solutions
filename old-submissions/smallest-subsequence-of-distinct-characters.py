class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = Counter(s)
        stack = []
        seen = set()

        for ch in s:
            count[ch] -= 1

            if ch in seen:
                continue

            while stack and stack[-1] > ch and count[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)