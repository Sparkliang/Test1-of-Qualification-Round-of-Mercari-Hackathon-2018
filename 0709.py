# to get the maxmium length of a sentence from a given string
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
        if c[t-1] == '':
            e = len(c) - 1
        elif c[0] == '':
            e = len(c) - 1
            #print(c)
        elif c[0] or c[t-1] == '':
            e = len(c) - 2
        else:
            e = len(c)
            #print(c)
        #print(i, e)
        d.append(e)
    return max(d)

#test
#S = 'Forget CVs..Save time . x x'
#solution(S)
#we will get 2
#S = 'We test coders. Give us a try'
#solution(S)
#we will get 4
