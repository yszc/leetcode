a = 'horse'
b = 'ors'
# b = 'ros'
class Solution:
    map = [[]]
    def minDistance(self, word1: str, word2: str) -> int:
        self.map = [[None for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        def editDiff(a, b):
            lena = len(a)
            lenb = len(b)
            if self.map[lena][lenb] != None:
                return self.map[lena][lenb]
            if lena == 0:
                self.map[lena][lenb] = lenb
                return self.map[lena][lenb]
            if lenb == 0:
                self.map[lena][lenb] = lena
                return self.map[lena][lenb]
            if a[lena-1] == b[lenb-1]:
                self.map[lena][lenb] = editDiff(a[:-1], b[:-1])
                return self.map[lena][lenb]
            else: 
                diff1 = editDiff(a, b[:-1])
                diff2 = editDiff(a[:-1], b)
                diff3 = editDiff(a[:-1], b[:-1])
                self.map[lena][lenb] = min(diff1,diff2,diff3)+1
                return self.map[lena][lenb]
        res = editDiff(word1, word2)
        print(self.map)
        return res



print(Solution().minDistance(a,b))