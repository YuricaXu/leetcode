class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()#sort children greedy factor
        s.sort()#sort cookie size
        j = len(s)-1 #from the last cookie
        result = 0 #how many children are content
        for i in range(len(g)-1,-1,-1):#from the last child
             if j >= 0 and s[j] >= g[i]:
                result +=1
                j-=1
        return result
