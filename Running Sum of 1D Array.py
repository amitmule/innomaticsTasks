class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = 0
        result = []
        
        for n in nums:
            running += n
            result.append(running)
        
        return result