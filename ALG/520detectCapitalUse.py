# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if len(word) == 1:
            return True
        elif len(word) == 2:
            if (word[0]<='z' and word[0] >= 'a') and (word[1]<='Z' and word[0] >= 'A'):
                return False
            return True
        else:
            if (word[1] < 'a' or word[1] > 'z') and (word[0]<='z' and word[0]>='a'):
                return False
            elif (word[1]<='z' and word[1] >= 'a'):
                j = 2
                while j < len(word):
                    if word[j] >'z' or word[j] < 'a':
                        return False
                    j += 1
                    if j == len(word):
                        return True
            elif (word[1]<='Z' and word[1] >= 'A'):
                j = 2
                while j < len(word):
                    if word[j] > 'Z' or word[j] < 'A':
                        return False
                    j += 1
                    if j == len(word):
                        return True


if __name__ == '__main__':
    a = "mCC"
    b = Solution()
    print (b.detectCapitalUse(a))
