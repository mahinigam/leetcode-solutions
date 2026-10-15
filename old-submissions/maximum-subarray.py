class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_sum = float('-inf')
        # s = 0

        # for i in range(len(nums)):
        #     s += nums[i]
        #     max_sum = max(s, max_sum)

        #     if s < 0:
        #         s = 0

        # return max_sum

        max_sum = nums[0]
        curr_max = 0

        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(curr_max, max_sum)

        return max_sum
