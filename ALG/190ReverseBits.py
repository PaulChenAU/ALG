# -*- coding:utf-8 -*-
# __author__=''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n is None:
            return
        a,j,k = list(bin(n)[2:].zfill(32)),1,0
        for i in range(5):
            while True:
                tmp = a[k:k+j]
                a[k:k+j] = a[k+j:k+2*j]
                a[k+j:k+2*j] = tmp
                k = k+2*j
                if k >= len(a):
                    break
            j = j * 2
            k = 0
        return int("0b"+"".join(a),2)


if __name__ == '__main__':
    a = Solution()
    print (a.reverseBits(0xff0011))
    print (bin(123))



'''
1234 5678
21436587
43218765





5678 1234
7856 3412
8765 4321
'''