class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        for i in range(2*min(len(word1),len(word2))):
            if(i%2==0):
                ans+=word1[0]
                word1 = word1[1:]
            else:
                ans+=word2[0]
                word2 = word2[1:]


        ans+=word1
        ans+=word2

        return ans