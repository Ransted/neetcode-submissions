class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        for i in range(n):
            fi = nums[i]
            ls = target -fi
            if ls in nums:
                j= nums.index(ls)
                break
        return [i,j]
        