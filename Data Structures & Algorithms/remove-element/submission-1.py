class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        count = 0
        while count< n:
            if nums[i] != val:
                i+=1
                count+=1
            elif nums[i] == val:
                nums.append(nums.pop(i))
                count+=1
        return i