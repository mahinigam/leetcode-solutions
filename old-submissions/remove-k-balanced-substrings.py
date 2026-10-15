class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        temp = s

        stack = []

        for ch in temp:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            else:
                stack[-1][1] += 1

            if len(stack) >= 2 and stack[-1][0] == ')' and stack[-2][0] == '(':
                while len(stack) >= 2 and stack[-1][0] == ')' and stack[-2][0] == '(':
                    open_count = stack[-2][1]
                    close_count = stack[-1][1]

                    to_remove = min(open_count, close_count, k)
                    if to_remove == k:
                        stack[-2][1] -= k
                        stack[-1][1] -= k

                        if stack[-2][1] == 0:
                            stack.pop(-2)
                        if stack and stack[-1][1] == 0:
                            stack.pop()
                    else:
                        break

        return ''.join(ch * cnt for ch, cnt in stack)