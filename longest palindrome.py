class Solution:
    def longestPalindrome(self, s: str) -> int:
        #dictionary for each letters occurance
        oc = {}
        res = 0
        odd = 0
        
        for char in s:
            if char not in oc:
                oc[char] = 1
            else:
                oc[char] += 1
                
        if len(oc) == 1:
            return oc[s[0]]
        
        for i in oc.values():
            if i > 1:
                if i%2 == 0:
                    res += i
                else:
                    res += i-1
                    odd += 1
            else:
                odd += 1
                
        if odd > 0:
            res += 1
        return res