class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        dup = -1
        mis = -1

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                dup = abs(num)
            else:
                nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res