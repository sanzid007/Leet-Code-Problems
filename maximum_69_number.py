class Solution:
    def maximum69Number (self, num: str) -> str:
        numStr = str(num)
        numStr = numStr.replace('6', '9', 1)
        
        return int(numStr)