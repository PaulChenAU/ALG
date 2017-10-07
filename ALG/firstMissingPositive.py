# -*- coding:utf-8 -*-
# __author__=''
# nums - list[int]
# rtype - int
class Solution(object):
    def firstMissingPositive(self, nums):
        if len(nums) == 0 or nums is None:
            return 0
        if len(nums) == 1:
            if nums[0] <= 0:
                return 1
            return nums[0] + 1
        i,n =0, len(nums)
        while i < n:
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != i:
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[nums[i]] = temp
            else:
                i += 1

if __name__ == '__main__':
    a = Solution()
    nums = [1,-1,9]
    print (a.firstMissingPositive(nums))

