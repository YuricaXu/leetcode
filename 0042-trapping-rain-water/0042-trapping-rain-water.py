class Solution:
    def trap(self, height: List[int]) -> int:
        leftheight, rightheight = [0]*len(height), [0]*len(height)

        leftheight[0]=height[0]
        for i in range(1,len(height)):
            #maxLeft[i] = max(height[i], maxLeft[i - 1]);
            leftheight[i]=max(leftheight[i-1],height[i])
        rightheight[-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            #right to left：maxRight[i] = max(height[i], maxRight[i + 1]);
            rightheight[i]=max(rightheight[i+1],height[i])

        result = 0
        for i in range(0,len(height)):
            summ = min(leftheight[i],rightheight[i])-height[i]
            result += summ
        return result