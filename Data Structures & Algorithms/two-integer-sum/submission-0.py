class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,n in enumerate(nums):
            if n not in seen:
                seen[target - n] = i
            else:
                return [seen[n], i]
            
        return 0
                
        