# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        if len(ops) == 0:
            return 0
        ans,l = 0,[]
        for i in range(len(ops)):
            if ops[i] == 'C':
                ans -= l.pop()
            elif ops[i] == 'D':
                ans += 2 * l[len(l)-1]
                l.append(2 * l[len(l)-1])
            elif ops[i] == '+':
                ans = ans + l[len(l)-2] + l[len(l)-1]
                l.append(l[len(l)-2]+l[len(l)-1])
            else:
                ans += int(ops[i])
                l.append(int(ops[i]))
        return ans



if __name__ == '__main__':
    a = Solution()
    print (a.calPoints(["36","28","70","65","C","+","33","-46","84","C"]))