class Solution:
    '''
    https://leetcode.com/problems/trapping-rain-water/solutions/3401992/100-detailed-explaination-with-pictures-in-c-java-python-two-pointers/
    '''
    def trap(self, height) -> int:
        sum = 0
        l = len(height)
        # height.append(0)
        lefts = [-1]*l
        rights = [-1]*l
        maxl = maxr = -1
        for i in range(l):
            if height[i] > maxl:
                maxl = height[i]
            lefts[i] = maxl

            if height[l-1-i] > maxr:
                maxr = height[l-1-i]
            rights[l-i-1] = maxr
        
        for i in range(l):
            sum += min(lefts[i], rights[i])-height[i]
        return sum



print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,0,3,2,5]))
print(Solution().trap([5,4,1,2]))
            
