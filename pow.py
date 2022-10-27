class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow = 1.00
        if n < 0:
            x = 1/x
            n = n * (-1)
            
        
        while n:
            if n &1:
                pow = pow * x
            n >>= 1
            x = x*x 

        return pow