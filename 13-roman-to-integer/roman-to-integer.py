class Solution:
    def romanToInt(self, s: str) -> int:
        val=0
        translate = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            if i+1<len(s) and translate[s[i]] < translate[s[i+1]]:
                val-=translate[s[i]]
                
            else:
                val+=translate[s[i]]
        return val