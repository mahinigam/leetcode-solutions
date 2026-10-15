class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_sorted = sorted(list(set(nums)))
        if len(nums_sorted) >= 3:
            return list(nums_sorted)[-3]
        else:
            return list(nums_sorted)[-1]