class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k%=n
        arr = [0] * n
        for i in range(len(arr)):
            arr[(k+i)%n] = nums[i]
        nums[:]=arr


