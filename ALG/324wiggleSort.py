# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums[::2])
        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]



if __name__ == '__main__':
    nums = [1, 3, 1, 2, 5, 6, 3, 7]
    nums2 = [4,5,5,6]
    s = Solution()
    s.wiggleSort(nums2)
