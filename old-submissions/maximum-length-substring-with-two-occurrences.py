class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # counts = {}

        # max_length = 0
        # left = 0

        # for right in range(len(s)):
        #     curr = s[right]
        #     counts[curr] = counts.get(curr, 0) + 1

        #     while counts[curr] > 2:
        #         left_char = s[left]
        #         counts[left_char] -= 1
        #         left += 1

        #     curr_window = right - left + 1
        #     max_length = max(max_length, curr_window)

        # return max_length

        counts_arr = [0] * 26

        max_length = 0
        left = 0

        for right in range(len(s)):
            right_idx = ord(s[right]) - ord('a')
            counts_arr[right_idx] += 1

            while counts_arr[right_idx] > 2:
                left_idx = ord(s[left]) - ord('a')
                counts_arr[left_idx] -= 1
                left += 1

            max_length = max(max_length, right-left+1)

        return max_length