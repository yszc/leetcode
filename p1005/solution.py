class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i,x in enumerate(A):
            if x < 0:
                A[i] = A[i] * -1
                K = K - 1
            if x >= 0 or K <= 0:
                break
            
        if K>0:
            if K % 2 == 1:
                if i == 0:
                    A[i] = A[i] * -1
                elif abs(A[i]) < abs(A[i-1]):
                    A[i] = A[i] * -1
                else:
                    A[i-1] = A[i-1] * -1
        return sum(A)
