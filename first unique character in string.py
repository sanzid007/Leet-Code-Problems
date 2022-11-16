from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=OrderedDict()
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i]=1
                
        for k,v in d.items():
            if v == 1:
                return s.index(k)
            
        return -1