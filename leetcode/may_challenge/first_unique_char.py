# 387

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,v in enumerate(s):
            if s.count(v) == 1:
                return i
        return -1
        
    def firstUniqChar2(self,s:str) -> int:
        charSet = set()
        dic = {}
        for i,v in enumerate(s):
            if v not in charSet:
                charSet.add(v)
                dic[v]=i
            elif v in dic:
                del dic[v]
        return -1 if not len(dic) else min(dic.values())
            