# -*- coding:utf-8 -*-
# __author__=''
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])


        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(i,val)
        # param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    num = [1,3,5]
    s = NumArray(num)
    print (s.sumRange(0,2))
    print(s.update(1,2))
    print(s.sumRange(0, 2))
