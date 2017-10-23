# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str] ..
        """
        num = sorted(nums,reverse=True)
        mylist = ["Gold Medal", "Silver Medal", "Bronze Medal"]+[str(i) for i in range(4,len(num)+1)]
        k = dict(list(zip(num,mylist)))
        return list(map(k.get,nums))





if __name__ == '__main__':
    a = Solution()
    print (a.findRelativeRanks([1]))
