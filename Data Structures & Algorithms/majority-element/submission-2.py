class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)
        return(nums[n//2])

        # after sorting the middle element of the list/array will be the majority 
        # element as number of majority element is more then n/2