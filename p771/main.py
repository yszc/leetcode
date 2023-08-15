class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        for c in jewels:
            dic[c] = True
        count = 0
        for c in stones:
            if c in dic.keys():
                count += 1
        return count

print(Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(Solution().numJewelsInStones(jewels = "z", stones = "ZZ"))