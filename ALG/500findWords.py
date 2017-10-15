# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        lista,listb,listc = set('zxcvbnm'),set('asdfghjkl'),set('qwertyuiop')
        for i in words:
            si = i.lower()
            seti = set(si)
            if seti.issubset(lista) or seti.issubset(listb) or seti.issubset(listc):
                ans.append(i)
        return ans


if __name__ == '__main__':
    a = Solution()
    print (a.findWords(["Hello","Alaska","Dad","Peace"]))