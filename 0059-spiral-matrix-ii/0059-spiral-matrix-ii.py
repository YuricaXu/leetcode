class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0]*n for _ in range(n)]
        startx, starty =0,0 #inital point
        loop, mid = n//2, n//2
        count=1#count

        for offset in range(1, loop+1):#loop
            for i in range(starty, n - offset):#from left to right
                nums[startx][i]=count
                count += 1
            for i in range(startx, n - offset) :    # form top to bottom 
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1) : # from tight to left
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1) : # from bottom to top
                nums[i][starty] = count
                count += 1                
            startx += 1         # renew
            starty += 1
        
        if n % 2 != 0 :			
            nums[mid][mid] = count 
        return nums