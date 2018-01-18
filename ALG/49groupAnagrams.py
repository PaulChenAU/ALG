# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        for _str in strs:
            s_str = sorted(_str)
            cmp_flag = 0
            for i in range(0,len(ans)):
                if s_str == sorted(ans[i][0]):
                    cmp_flag = 1
                    ans[i].append(_str)
            if len(ans) == 0 or cmp_flag == 0:
                result = []
                result.append(_str)
                ans.append(result)
        return ans




if __name__ == '__main__':
    lstr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    a = Solution()
    print(a.groupAnagrams(lstr))

