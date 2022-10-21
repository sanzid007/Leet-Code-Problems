class Solution:
    def largestPerimeter(self, num: List[int]) -> int:
        num.sort(reverse = True)
        for i in range(len(num)-2):
            if num[i] < num[i+1] + num[i+2]:
                return num[i]+num[i+1]+num[i+2]
        return 0