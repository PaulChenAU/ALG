# -*- coding:utf-8 -*-
# __author__=''
"""
:type nums1: List[int]
:type m: int
:type nums2: List[int]
:type n: int
:rtype: void Do not return anything, modify nums1 in-place instead.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m+n-1] = nums1[m-1]
        if m == 0 or nums1[0] == 0:
            nums1.pop()
            for i in range(0,n):
                nums1.append(nums2[i])
        else:
            num = [0 for x in range(0,m+n)]
            i,j,pre = 0,0,0
            while True:
                if i == m:
                    break
                elif j == n:
                    break
                print ("i,j,pre =",i,j,pre)
                if nums1[i] <= nums2[j]:
                    num[pre] = nums1[i]
                    i += 1
                    pre += 1
                else:
                    num[pre] = nums2[j]
                    j += 1
                    pre += 1
            if i == m and j != n:
                while True:
                    if j == n:
                        break
                    num[pre] = nums2[j]
                    pre += 1
                    j += 1
            elif j == n and i != m:
                while True:
                    if i == m:
                        break
                    num[pre] = nums1[i]
                    pre += 1
                    i += 1
            nums1 = num
        print (nums1)




if __name__ == '__main__':
    num = [1,1,2,3,4,5]
    print (num)
    nums = [1,2,3,3]
    a = Solution()
    ta = [1,2,3,4]
    tb = [2,4,6]
    print (ta[:0+1])