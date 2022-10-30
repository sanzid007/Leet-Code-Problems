class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        num = []
		
        for i in range(1, n):
            fact *= i # store the total number of factorials
            num.append(i)
        num.append(n)
		
        ans = ''
        k = k - 1
		
		# In every while loop we will have the left most number 
        while True:
            x = num[k // fact]
            ans = ans + str(x)
            num.remove(x)
            if not num:
                break
            k = k % fact
            fact = fact // len(num)
			
        return ans