# -*- coding:utf-8 -*-
# __author__=''
import math
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) <= 2:
            m = len(nums)
        else:
            m = int(math.log(len(nums)-1,2)) + 2
        self.segTree = [0 for i in range(2**m-1)]
        self.height = len(nums)
        if len(nums) > 0:
            self.build(0, nums, 0, len(nums)-1)

    def build(self, root ,nums, begin, end):
        if begin == end:
            self.segTree[root] = nums[begin]
        else:
            mid = int((begin + end)/2)
            self.build(root*2+1 , nums, begin, mid)
            self.build(root*2+2, nums, mid+1, end)
            self.segTree[root] = self.segTree[root*2+1] + self.segTree[root*2+2]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums(0,self.height-1,i,j,0)

    def sums(self,left,right,i,j,m):
        if left == i and right == j:
            return self.segTree[m]
        else:
            mid = int((left+right)/2)
            if i <= mid and j > mid:
                return self.sums(left, mid, i, mid, m*2+1)+self.sums(mid+1,right,mid+1,j,m*2+2)
            elif j <= mid:
                return self.sums(left, mid ,i, j,m*2+1)
            else:
                return self.sums(mid+1,right,i,j,m*2+2)

if __name__ == '__main__':
    a = NumArray([-2, 0, 3, -5, 2, -1])
    print (a.segTree)
    print (a.sumRange(2,5))
    b = NumArray([])
    print (b.segTree)
#            0-5
#        0-2   3-5
#     0-1   2 3-4  5
#
#    0-2
#   0-1 1-2



#    1
#  -2  3    -3 -1
# -2 0  3  -5 2
#
#
#  0-0
#  1-1
#  2-2
#  3-3
#  4-3
#  5-4
#  6-4
#  7-4
#  8-5
#  9-5
#  10-5
#  11-5
#  12-5
#  13-5
#  14-5
#  15-5
#  16-5
#  17-6
