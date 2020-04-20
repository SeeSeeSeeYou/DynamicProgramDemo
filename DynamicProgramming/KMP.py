import numpy as np

class KPM(object):
    """description of class"""

#首先获取 prefix table
#然后再进行移位
#然后进行对比
def prefix_table(pattern,prefix,n):
    prefix[0] = 0
    len = 0 
    i = 1
    while i < n:
        if pattern[i] == pattern[int(len)]:
            len = len + 1
            prefix[i] = len
            i = i + 1
        else:
            if len > 0:
                len = prefix[int(len - 1)]
            else:
                prefix[i] = len
                i = i + 1

def move_prefix_table(prefix,n):
    for i in range(len(prefix) - 1,2,-1): 
        prefix[i] = prefix[i - 1]
    prefix[0] = -1

def kmp_search(pattern, text):
    n = len(pattern)
    prefix = n * [0]
    prefix_table(pattern,prefix,n)
    move_prefix_table(prefix,len) 
    m = len(text)
    i = 0
    j = 0
    while(i < m):
        if j == n - 1 and text[i] == pattern[j]:
            print("Found at",i - j)
            j = prefix[j]
        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1
        else:
            j = prefix[j]
            if j == -1:
                i = i + 1
                j = j + 1 

pattern = 'ABABCABAA'
text = 'ABABABCABAABABABAB'
kmp_search(pattern,text)


