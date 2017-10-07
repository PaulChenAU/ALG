# -*- coding:utf-8 -*-
# __author__=''
# a -- str  b-- str  rtype -- str
class Solution(object):
    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]
        i = 0
        c = ""
        LastAdd = 0
        mode = 0
        while True:
            if i == len(a) or i == len(b):
                if i == len(a) and i == len(b):
                    mode = 0
                elif i == len(a) and i != len(b):
                    mode = 1
                elif i != len(a) and i == len(b):
                    mode = 2
                break
            NumStr = int(a[i]) + int(b[i]) +LastAdd
            if NumStr == 2:
                NumStr = 0
                LastAdd = 1
            elif NumStr == 3:
                NumStr = 1
                LastAdd = 1
            else:
                LastAdd = 0
            c += str(NumStr)
            i += 1
        if mode == 1:
            for i in range(len(a),len(b)):
                NumStr = int(b[i]) + int(LastAdd)
                if NumStr == 2:
                    LastAdd = 1
                    NumStr = 0
                else:
                    LastAdd = 0
                c += str(NumStr)
        elif mode == 2:
            for i in range(len(b),len(a)):
                NumStr = int(a[i]) + int(LastAdd)
                if NumStr == 2:
                    LastAdd = 1
                    NumStr = 0
                else:
                    LastAdd = 0
                c += str(NumStr)
        if LastAdd == 1:
            c += str(LastAdd)
        return c[::-1]



if __name__ == '__main__':
    a = "101010"
    b = "110101"
    c = Solution()
    print (c.addBinary(a,b))