class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        pos = 0
        neg = 0
        
        for x in nums:
            pos += x
            neg += x
            if pos < 0:
                pos = 0
            if neg > 0:
                neg = 0
                
            res = max(res, pos, abs(neg))
        
        return res