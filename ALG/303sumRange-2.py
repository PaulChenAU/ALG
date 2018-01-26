# -*- coding:utf-8 -*-
# __author__=''
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0 for i in range(len(nums))]
        if len(nums) > 0:
            self.sums[0] = nums[0]
        for i in range(1,len(nums)):
            self.sums[i] = self.sums[i-1] + nums[i]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]


if __name__ == '__main__':
    a = NumArray([1,2,3,4,5,6])
    print (a.sumRange(0,0))
    b = NumArray([])
