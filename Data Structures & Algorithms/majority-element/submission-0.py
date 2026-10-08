class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = {}
        for i in range(len(nums)):
            if nums[i] not in maj:
                maj[nums[i]] = 1
            else:
                maj[nums[i]]+= 1
        return max(maj, key = maj.get)