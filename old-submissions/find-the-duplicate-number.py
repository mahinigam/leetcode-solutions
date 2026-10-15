class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == 2:
                return num