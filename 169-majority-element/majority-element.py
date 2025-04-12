class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        maj = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == maj:
                count+=1
            else:
                count-=1
            if count == 0:
                maj=nums[i]
                count+=1

        return maj

