class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h ={}
        n = len(nums)
        for i in range(n):
            if (target-nums[i]) not in h:
                h[nums[i]] = i
            else:
                return [h[target-nums[i]],i]
        