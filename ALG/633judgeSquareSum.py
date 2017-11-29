import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        while a <= int(math.sqrt(c)):
            b = int(math.sqrt(c - a*a))
            if b*b + a*a == c:
                return True
            a = a + 1
        return False



if __name__ == '__main__':
    a = Solution()
    print a.judgeSquareSum(3)