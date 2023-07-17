class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        # 下标对齐
        num1 = num1[::-1]
        num2 = num2[::-1]
        sum = ''
        i = 0
        posSum = 0
        # 退出条件：计算完短的数，且进位不为 0
        while i < len1 and i < len2 or posSum>0:
            posSum += int(num1[i] if i<len1 else 0) + int(num2[i] if i<len2 else 0)
            sum += str(posSum % 10)
            posSum = posSum // 10
            i += 1
        # 未参与计算的部分直接追加
        if i < len1:
            sum += num1[i:]
        if i < len2:
            sum += num2[i:]
        return sum[::-1]
    

s = Solution()
print(s.addStrings('123', '11'))
print(s.addStrings('777', '456'))
print(s.addStrings('0', '0'))