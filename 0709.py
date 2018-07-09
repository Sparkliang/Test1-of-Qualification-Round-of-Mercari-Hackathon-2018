def solution(S):
    # write your code in Python 3.6
    import re
    a = re.split(r'[.?!]', S)
    n = len(a)
    d = []
    for i in range(n):
        b = a[i]
        c = re.split(r'[ ]', b)
        t = len(c)
        if c[t - 1] == '':
            e = len(c) - 1
        elif c[0] == '':
            e = len(c) - 1
            #print(c)
        else:
            e = len(c)
            #print(c)
        #print(i, e)
        d.append(e)
    return max(d)
