class Solution:
    def lemonadeChange(self, bills) -> bool:
        '''
        钱包字典 wallet 定义了所有可以被用于找零的币种，key是面值，value 是初始状态的数量。本题只有 5,10 两种面值可以找零，且均为 0 张。
        采用贪心策略，每次找零都从最大面值的币种开始，最多可找零 余额//面值 的数量，依次遍历到最小面值，如果余额还不为0，则无法正确找零。
        '''
        wallet = {5:0, 10:0}
        for bill in bills:
            # 入钱包
            if bill in wallet.keys():
                wallet[bill] += 1
            # 消费 5 元
            bill -= 5
            # 根据面值从大到小依次找零
            for v in sorted(wallet.keys(),reverse=True) :
                nums = min(wallet[v], bill//v)
                wallet[v] -= nums
                bill -= nums*v
            if bill>0:
                return False
        return True

print(Solution().lemonadeChange([5,5,5,10,20]))
print(Solution().lemonadeChange([5,5,10,10,20]))