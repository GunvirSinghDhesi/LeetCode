class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1

        while j<len(nums): # means we have found all the unique values
            if nums[j] == nums[j-1]: #keep going through the list until nums[i] is not the same as the element before
                j+=1
            else: # found unique number
                i+=1 # i only increases everytime a new unique number is found
                nums[i]=nums[j]
                j+=1
        return i+1 # is the number of unique numbers found + 1 (since we ignore the first unique number)
