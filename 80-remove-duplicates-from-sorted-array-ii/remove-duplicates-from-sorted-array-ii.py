class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2 # stays on last tripple site

        for i in range(2, len(nums)):
            if nums[k-2] != nums[i]:
                nums[k] = nums[i]
                k+=1 # only increase to the next site, so we can continue replacing.
        return k