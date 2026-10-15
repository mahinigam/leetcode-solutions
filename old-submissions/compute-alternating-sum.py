class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even = []
        odd = []

        for i in range(0, len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        return sum(even) - sum(odd)