class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(current, start):
            if len(current)==4:
                if start==len(s):   output.append(current)
            for i in range(start, min(start+3, len(s))):
                if s[start]==0 and i>start:
                    continue
                if 0<=int(s[start:i+1])<=255:
                    backtrack(current+s[start:i+1], start+1)
        output=[]
        backtrack('', 0)
        return output