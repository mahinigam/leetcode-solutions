class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        R_VAL = 100000

        s = sorted(nums)

        l1, l2, l3 = s[-1], s[-2], s[-3]
        s1, s2 = s[0], s[1]

        prod_A = max(l1 * l2 * l3, s1 * s2 * l1)
        max_prod_2 = max(l1 * l2, s1 * s2)
        min_prod_2 = s1 * l1

        prod_B1 = max_prod_2 * R_VAL
        prod_B2 = max_prod_2 * (-R_VAL)
        prod_B3 = min_prod_2 * R_VAL
        prod_B4 = min_prod_2 * (-R_VAL)

        return max(prod_A, prod_B1, prod_B2, prod_B3, prod_B4)