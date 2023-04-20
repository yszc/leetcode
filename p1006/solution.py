class Solution:
    def getTerm3(self, N: int, f: bool) -> int:
        if N <= 0:
            return 0
        res = N
        if N - 1 > 0:
            res = res * (N-1)
        if N - 2 > 0:
            res = int(res / (N-2))
        if N - 3 > 0:
            if f:
                res = res + (N-3)
            else:
                res = res - (N-3)
        return res
    def clumsy(self, N: int) -> int:
        res = self.getTerm3(N, True)
        while N > 4:
            N = N - 4
            res = res - self.getTerm3(N, False)
        return res
            
