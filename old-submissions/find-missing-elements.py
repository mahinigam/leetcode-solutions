class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val, max_val = min(nums), max(nums)
        nums_set = set(nums)
        ans = []

        for i in range(min_val+1, max_val):
            if i not in nums_set:
                ans.append(i)

        return ans