# -*- coding:utf-8 -*-
# __author__=''
"""
:type nums: List[int]
:rtype: int
"""
class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0 or nums is None:
            return
        if len(nums) == 1:
            return nums[0]
        last = nums[0]
        for i in range(1,len(nums)):
            if last + nums[i] > nums[i]:
                nums[i] = last + nums[i]
            last = nums[i]
        max = nums[0]
        for i in range(0,len(nums)):
            if nums[i] > max:
                max = nums[i]
        return max




if __name__ == '__main__':
    a = Solution()
    print (a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
