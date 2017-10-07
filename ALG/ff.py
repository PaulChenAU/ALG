#:type s: str
#:rtype: bool
def isValid(s):
    if len(s) == 1 or len(s) == 0 or s is None:
        return False
    a = []
    for i in range(0,len(s)):
        a.append(0)
    k = 0
    flag = 1
    while k <= len(s) - 1:
        if s[k] == '}':
            l = k - 1
            while l >= 0:
                if a[l] == 0:
                    break
                else:
                    l -= 1
            if s[l] == '{':
                a[k] = 1
                a[l] = 1
            else:
                flag = 0
                break
        if s[k] == ']':
            l = k - 1
            while l >= 0:
                if a[l] == 0:
                    break
                else:
                    l -= 1
            if s[l] == '[':
                a[k] = 1
                a[l] = 1
            else:
                flag = 0
                break
        if s[k] == ')':
            l = k - 1
            while l >= 0:
                if a[l] == 0:
                    break
                else:
                    l -= 1
            if s[l] == '(':
                a[k] = 1
                a[l] = 1
            else:
                flag = 0
                break
        k += 1
    for i in range(0,len(s)):
        if a[i] == 0:
            flag = 0
    if flag == 0:
        return False
    return True


if __name__ == '__main__':
    s = '{()}'
    print (isValid(s))