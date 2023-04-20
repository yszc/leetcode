class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        l = len(A)
        ra = rb = 0
        fa = A[0]
        fb = B[0]
        i = 1
        same = 0
        while i < l:
            if ra >= 0:
                if fa == A[i]:
                    ra
                elif fa == B[i]:
                    ra = ra + 1
                else:
                    ra = -1

            if rb >= 0:
                if fb == B[i]:
                    rb
                elif fb == A[i]:
                    rb = rb + 1
                else:
                    rb = -1
            if A[i] == B[i]:
                same += 1
            # print('r',ra,rb)
            if ra == -1 and rb == -1:
                return -1
            i += 1
            
        if ra >= 0:
            ra = min(ra, l - ra - same)
        if rb >= 0:
            rb = min(rb, l - rb - same)
        print (ra,rb,same)
        if rb < 0:
            return ra
        if ra < 0:
            return rb
        if ra >= 0 and ra <= rb:
            return ra
        if rb >= 0 and rb <= ra:
            return rb
        return -1
