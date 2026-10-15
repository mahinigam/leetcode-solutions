class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        res = []

        for i in range(len(nums)):
            res.append(temp.index(nums[i]))

        return res