# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def plusOne(self, digits):
        if digits is None or len(digits) == 0:
            return
        LastAdd = 0
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits) - 1:
                digits[i] += 1
                if digits[i] == 10:
                    digits[i] = 0
                    LastAdd = 1
            else:
                digits[i] += LastAdd
                if digits[i] == 10:
                    digits[i] = 0
                    LastAdd == 1
                else:
                    LastAdd = 0
        if LastAdd == 0:
            return digits
        else:
            digits.append(0)
            for i in range(len(digits) - 1,0,-1):
                digits[i] = digits[i-1]
            digits[0] = 1
            return digits

if __name__ == '__main__':
    a = Solution()
    digits = [9]
    print (a.plusOne(digits))