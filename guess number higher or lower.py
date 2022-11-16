class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        while s <= n:
            x = (n + s) // 2
            g = guess(x)
            
            if g == 0 : 
                return x
            if g < 0  :
                n = x - 1
            if g > 0  :
                s = x + 1