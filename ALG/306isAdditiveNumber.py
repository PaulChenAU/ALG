# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        for i in range(1,int(len(num)/2)+1):
            for j in range(i+1,i+int(len(num)/2)+1):
                if len(num[0:i]) == 1 or (len(num[0:i]) > 1 and num[0:i].startswith('0') is False):
                    if len(num[i:j]) == 1 or (len(num[i:j]) > 1 and num[i:j].startswith('0') is False):
                        numa, numb = int(num[0:i]), int(num[i:j])
                        if self.judgeAdditive(numa, numb, num[j:len(num)]) is True:
                            return True

        return False

    def judgeAdditive(self,numa,numb,num):
        sums = numa + numb
        sums_str = str(sums)
        if num.startswith(sums_str):
            if len(num) - len(sums_str) == 0:
                return True
            else:
                return self.judgeAdditive(numb, sums, num[len(sums_str):len(num)])
        else:
            return False




if __name__ == '__main__':
    a = Solution()
    print (a.isAdditiveNumber("12305"))
    print (a.judgeAdditive(1,2,"3581321"))
    str_begin = "11"
    i , j = 0,1



