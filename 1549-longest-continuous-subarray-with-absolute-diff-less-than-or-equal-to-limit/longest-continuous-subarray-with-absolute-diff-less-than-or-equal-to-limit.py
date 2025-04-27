class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        
        maxDeque = deque()
        minDeque = deque()
        left = 0
        result = 0

        for right in range(len(nums)):
            # Maintain maxDeque (decreasing)
            while maxDeque and nums[right] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[right])

            # Maintain minDeque (increasing)
            while minDeque and nums[right] < minDeque[-1]:
                minDeque.pop()
            minDeque.append(nums[right])

            # If window is invalid, shrink it from left
            while maxDeque[0] - minDeque[0] > limit:
                if maxDeque[0] == nums[left]:
                    maxDeque.popleft()
                if minDeque[0] == nums[left]:
                    minDeque.popleft()
                left += 1

            # Update result
            result = max(result, right - left + 1)

        return result