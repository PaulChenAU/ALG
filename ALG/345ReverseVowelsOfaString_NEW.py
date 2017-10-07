# -*- coding:utf-8 -*-
# __author__=''
import re
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = re.findall('[aAeEiIoOuU]',s) #return List
        return re.sub('[aAeEiIoOuU]',lambda x:vowel.pop(),s)

if __name__ == '__main__':
    s = 'leetcodE'
    vowels = re.findall('[aeiou]', s)
    a = Solution()
    print (a.reverseVowels(s))

    str = 'abcde'
    #list = lambda x: str.pop()
    #print (list(0))

