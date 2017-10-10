# -*- coding:utf-8 -*-
# __author__=''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low,high = 1,n
        while low <= high:
            mid = low + int((high-low)/2)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid - 1
            else:
                low = mid + 1



if __name__ == '__main__':
    a = Solution()
    print (a.guessNumber(10))