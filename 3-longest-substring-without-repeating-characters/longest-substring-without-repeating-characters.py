class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0  
        left=0
        cur = {}

        right = 0
        while right < len(s):
            if s[right] in cur:
                maxLen=max(maxLen, len(cur))
                left+=1
                right=left

                cur={}

                cur[s[left]]=len(cur)
                
            else:
                cur[s[right]]=len(cur)

            right+=1
    
        maxLen=max(maxLen, len(cur))
        return maxLen
            
            