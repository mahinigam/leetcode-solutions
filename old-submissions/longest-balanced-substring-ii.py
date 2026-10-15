import collections

class Solution:
    def longestBalanced(self, s: str) -> int:
        temp = s
        max_len = 0

        def helper(state_fn):
            nonlocal max_len
            counts = {'a':0, 'b':0, 'c':0}
            state_map = {state_fn(0, 0, 0): -1}

            for i, ch in enumerate(temp):
                counts[ch] += 1
                ca, cb, cc = counts['a'], counts['b'], counts['c']

                current_state = state_fn(ca, cb, cc)

                if current_state in state_map:
                    max_len = max(max_len, i - state_map[current_state])
                else:
                    state_map[current_state] = i

        state_conditions = [
            lambda ca, cb, cc: (ca-cb, ca-cc),
            lambda ca, cb, cc: (ca-cb, cc),
            lambda ca, cb, cc: (ca-cc, cb),
            lambda ca, cb, cc: (cb-cc, ca),
            lambda ca, cb, cc: (cb, cc),
            lambda ca, cb, cc: (ca, cc),
            lambda ca, cb, cc: (ca, cb),
        ]

        for condition in state_conditions:
                helper(condition)

        
        return max_len