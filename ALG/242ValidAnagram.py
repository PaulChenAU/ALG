# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dics = {}
        dict = {}
        for index,item in enumerate(s):
            if item not in dics:
                dics[item] = 1
            else:
                dics[item] += 1
        for index,item in enumerate(t):
            if item not in dict:
                dict[item] = 1
            else:
                dict[item] += 1
        return (dict == dics and t != s) or (len(t)==len(s)==0)



if __name__ == "__main__":
    a = Solution()
    s = "";
    t = "";
    print (1==1==1)
    print (a.isAnagram(s,t))
