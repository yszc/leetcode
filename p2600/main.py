import sys

ones = int(sys.stdin.readline())
zeros = int(sys.stdin.readline())
negs = int(sys.stdin.readline())

k = int(sys.stdin.readline())


def maxBag(items, k: int) -> int:
    '''
    构建权重和物品数的字典items，用贪心策略，优先取权重高的物品
    '''
    sum = 0
    for w, n in sorted(items.items(), key=lambda x:x[0], reverse=True):
        sum += min(n, k) * w
        k -= min(n, k)
        if k == 0:
            break
    return sum

print(maxBag({1:ones, 0: zeros, -1: negs}, k))

