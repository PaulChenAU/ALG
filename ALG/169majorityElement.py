# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def majorityElement(self, nums):
        return sorted(nums)[int(len(nums)/2)]
        # Leans on assumption that a majority element exists
        #return sorted(nums)[(len(nums) // 2) - 1 + len(nums) % 2]


if __name__ == '__main__':
    a = Solution()
    list = [2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1]
    list2 = [2,2]
    print (a.majorityElement(list))
    print (5//2)
