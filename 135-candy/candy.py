class Solution:
    def candy(self, ratings: List[int]) -> int:

        nArr=[1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1]<ratings[i]:
                nArr[i]+=nArr[i-1]

        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1]>ratings[i] and nArr[i-1]<=nArr[i]:
                nArr[i-1]=nArr[i]+1

        totalCandies = sum(nArr)
        return totalCandies