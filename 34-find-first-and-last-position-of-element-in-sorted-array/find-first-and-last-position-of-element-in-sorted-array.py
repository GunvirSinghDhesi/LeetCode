class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        found=0
        left = 0
        right = len(nums)-1
        middle = (left+right)//2
        print(f"{left} {middle} {right} {nums}")

        while True:
            if left > right:
                break
            # If middle = target, bring left and right in
            if target==nums[middle]:
                found=1
                while nums[right] !=target:
                    right-=1
                while nums[left]!=target:
                    left+=1
                break
            # Move either left or right in
            elif(target>nums[middle]):
                left = middle+1
                middle =  (left+right)//2
            elif target<nums[middle]:
                right = middle-1
                middle =  (left+right)//2


    
        print(ans)
        ans = [left,right] if found else ans
        return ans