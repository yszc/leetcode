import sys

class Solution:
    '''
    设：P(row,col)为 row,col 位置开始向下的最小路径和，m(row,col)为矩阵上 row,col 位置的数字
    首先用搜索算法的思路来看，如果暴力枚举法，则有：
    P(row,col) = m(row,col) + min[ P(row+1,col-1), P(row+1,col), P(row+1,col+1) ]
    很明显这像一个状态转移公式，于是用动态规划的思路提高效率，先算出所有的 P(row+1,...)，则 P(row,col)可以很快得出。
    以上状态转移公式为自下向上递推。因为路线并没有方向，因此我们也可以自上向下递推。则状态转移公式为：
    P(row,col) = m(row,col) + min[ P(row-1,col-1), P(row-1,col), P(row-1,col+1) ]
    边界条件：
    row=0时有：P(row,col) = m(row,col)
    
    '''
    def minFallingPathSum(self, matrix) -> int:
        n = len(matrix)
        res = [[None for i in range(n)] for j in range(n)]
        for row in range(n):
            for col in range(n):
                if row == 0:
                    res[row][col] = matrix[row][col]
                else:
                    res[row][col] = min(res[row-1][col], res[row-1][max(0, col-1)], res[row-1][min(col+1, n-1)])+matrix[row][col]
        return min(res[n-1])
            

print(Solution().minFallingPathSum([
    [2,1,3],[6,5,4],[7,8,9]
]))