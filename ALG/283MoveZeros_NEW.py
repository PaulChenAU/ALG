# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 1:
            i = 0
            for num in nums:
                if num != 0:
                    nums[i] = num
                    i += 1
            for j in range(i,len(nums)):
                nums[j] = 0

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    a = Solution()
    a.moveZeroes(nums)
    print (nums)