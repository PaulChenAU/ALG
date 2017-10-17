# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 2:
            nums.sort()
            return nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3] if nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3]>nums[len(nums)-1]*nums[0]*nums[1] else nums[len(nums)-1]*nums[0]*nums[1]
        return None


if __name__ == '__main__':
    a = Solution()
    print (a.maximumProduct([-1,-2,-3]))