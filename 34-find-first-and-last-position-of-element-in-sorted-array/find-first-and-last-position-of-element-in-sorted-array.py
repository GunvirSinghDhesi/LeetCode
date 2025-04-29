class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        found=0
        left = 0
        right = len(nums)-1
        middle = (left+right)//2

        fr=-1
        lr=-1
        #to find right
        while left <= right:
            # If middle = target, bring left and right in
            if target==nums[middle]:
                fr=middle   
                found = 1
                left = middle+1
                middle = (left+right)//2
            # Move either left or right in
            elif(target>nums[middle]):
                left = middle+1
                middle =  (left+right)//2
            elif target<nums[middle]:
                right = middle-1
                middle =  (left+right)//2

        left = 0
        right = len(nums)-1
        middle = (left+right)//2

        #to find left
        while left <= right:
            # If middle = target, bring left and right in
            if target==nums[middle]:
                lr=middle   
                found = 1
                right = middle-1
                middle = (left+right)//2
            # Move either left or right in
            elif(target>nums[middle]):
                left = middle+1
                middle =  (left+right)//2
            elif target<nums[middle]:
                right = middle-1
                middle =  (left+right)//2


    
        print(ans)
        ans = [lr,fr] if found else ans
        return ans