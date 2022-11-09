class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in complementMap:
                return [i, complementMap[num]]
            else:
                complementMap[complement] = i