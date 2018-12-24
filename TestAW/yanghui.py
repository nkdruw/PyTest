#coding=utf-8

'''
杨辉三角(a+b)**n期待输出:
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
'''

def yanghui(m,n):

    if m<n or m<0 or n<0:
        raise 0
    else:

        s = [1]
        i = 0
        while i<m:
            t = s
            t.append(0)
            s = [t[j-1]+t[j] for j in range(len(t))]
            i += 1
        return s[n]