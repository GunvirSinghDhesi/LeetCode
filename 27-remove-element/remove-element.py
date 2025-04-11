class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rptr = len(nums) - 1
        lptr = len(nums) - 1
        k = len(nums)
        while True:
            if lptr < 0:
                break
            if nums[lptr] == val:
                k-=1
                if lptr != rptr:
                    # nums[lptr] = 0
                    del nums[lptr]
                    # nums[lptr] = nums[rptr]
                    # nums[rptr] = 0
                    rptr -= 1

                else:
                    # nums[lptr] = 0
                    del nums[lptr]
                    rptr-=1
            
            lptr -= 1
