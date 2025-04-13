class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas=0
        for newGas in nums:
            if gas<0:
                return False
            elif newGas > gas:
                gas = newGas


            gas-=1
        return True
            
            
        
        return False



