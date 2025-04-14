class Solution:
    def jump(self, nums: List[int]) -> int:
        totalJumps = 0
        currentEnd = 0 # how far can we get with the current jump
        furthestIndex = 0

        for i in range(len(nums) - 1):
            furthestIndex = max(furthestIndex, i + nums[i])

            if i == currentEnd:
                totalJumps += 1
                currentEnd = furthestIndex


        return totalJumps