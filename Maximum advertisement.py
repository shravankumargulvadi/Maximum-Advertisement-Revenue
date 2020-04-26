
# coding: utf-8

# In[8]:


import numpy as np
import sys
def max_ad_rev(a,b):
    a=np.sort(a)
    b=np.sort(b)
    c=a*b
    d=np.sum(c)
    return d


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_ad_rev(a, b))

