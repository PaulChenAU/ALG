# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        ans = max(self.dp(nums, len(nums) - 1))
        return ans

    def dp(self, nums, i):
        if i == -1:
            return 0, 0

        lastdfs = self.dp(nums, i - 1)
        iNotInclude, iIncluded = max(lastdfs), nums[i] + lastdfs[0]
        return iNotInclude, iIncluded


if __name__ == '__main__':
    s = Solution()
    print(s.rob([4, 1, 2, 3]))
