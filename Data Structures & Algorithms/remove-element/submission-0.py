class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        for n in nums:
            if n == val:
                nums.pop(n)
        k = len(nums)
        return(k)