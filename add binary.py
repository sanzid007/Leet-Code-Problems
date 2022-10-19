class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        carry = 0
        a,b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            num_A = ord(a[i]) - ord("0") if i<len(a) else 0
            num_B = ord(b[i]) - ord("0") if i<len(b) else 0
            
            total = num_A + num_B + carry
            char = str(total % 2)
            output = char + output
            carry = total // 2
            
        if carry:
            output = "1" + output
        
        return output