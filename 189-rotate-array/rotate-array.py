class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k%=len(nums)
        arr = [0] * len(nums)
        for i in range(len(arr)):
            arr[(k+i)%len(nums)] = nums[i]
        nums[:]=arr


