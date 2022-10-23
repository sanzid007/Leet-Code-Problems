class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(map(int, sorted(str(num), reverse=True)))
        
        output = 0
        pos = 0
        for i in range(len(num)):
            output += num[i] * 10**pos
            if i%2:
                pos+=1
                
        return output