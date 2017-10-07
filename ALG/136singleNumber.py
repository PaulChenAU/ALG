# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        i = 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i] and nums[i+2] != nums[i]:
                i += 2
            else:
                return nums[i]
        return nums[i]

    def sn2(self,nums):
        n = 0
        for i in nums:
            n = n ^ i
        return n
    def isPowerOfFour(self,n):
        return (not (n&(n-1))) and (n&0x55555555)>0
    def nsamexor(self,n):
        p = 0
        for i in n:
            p = p ^ ord(i)
            print (p)
        return chr(p)

    def nsamexor2(self,n):
        p = 0
        for i in n:
            p = p ^ i
            print (p)
        print ('-------')
        return p


if __name__ == '__main__':
    a = Solution()
    nums = [1,1,2,2,3,3,7,5,5]
    print (a.sn2(nums))
    b = 7
    print (b ^ 2)
    print ('------------------')
    sum = [1,1,3,3,2,4,4,2,6]
    #sum = 'abcab'
    print (a.nsamexor2(sum))

