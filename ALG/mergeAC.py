# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j,pre = m-1,n-1,m+n-1
        while i > -1 and j > -1:
            if nums1[i] >= nums2[j]:
                nums1[pre] = nums1[i]
                i -= 1;pre -=1
            else:
                nums1[pre] = nums2[j]
                j -= 1;pre -=1
        if j > -1:
            nums1[:j+1] = nums2[:j+1]