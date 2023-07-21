import heapq
class Solution:
    '''
    最朴素的方法是用每一个 query 查询每一个 interval，找到最短的区间。但是这样时间效率比较低，我们采用几个优化策略。
    首先我们根据 interval 的左侧排序，再把 query 排序，则有：
        A：某个 interval.left<query[i] 一定 interval.left<query[i+1] interval.left<query[i+2] ...
        B：某个 interval.right<query[i]一定 interval.right<query[i+1] interval.right<query[i+2] ...
    根据 A 帮我们选出符合 query[i] ... query[n] 的 interval 的准入条件
    根据 B 帮我们选出符合 query[i] ... query[n] 的 interval 的准出条件
    在所有符合 A 的 interval 里面，我们按照(interval长度, interval.left, interval.right)排序来维护一个优先队列 pq，从最短的 interval 依次检查 B ，如不符合则剔除，如符合则是答案所在。
    
    接下来，就是如何维护优先队列pq的排序，如果每加一个 interval 就做一次排序，则时间复杂度又成了 n*nlog，这个时候我们找到了 heap，他可以确保最顶端的元素永远是最小的，而heap可以使得前面过程变成 nlogn
    '''

    def minInterval(self, intervals, queries):
        pq = []
        qindex = list(range(len(queries)))
        qindex.sort(key=lambda x: queries[x])
        intervals.sort(key=lambda x: x[0])
        
        res = [-1] * len(queries)
        i = 0
        for qi in qindex:
            while i<len(intervals) and queries[qi]>=intervals[i][0]:
                heapq.heappush(pq, (intervals[i][1]-intervals[i][0]+1, intervals[i][0], intervals[i][1]))
                i += 1
            
            while len(pq)>0 and queries[qi]>pq[0][2]:
                heapq.heappop(pq)
            
            if len(pq)>0:
                res[qi] = pq[0][0]
        return res
            
            
    
# print(Solution().minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]))
print(Solution().minInterval(intervals = [[2,3],[2,5],[2,4],[3,5],[4,6],[1,8],[20,25]], queries = [2,19,5,22]))
# print(Solution().minInterval(intervals = [[9,9],[6,7],[5,6],[2,5],[3,3]], queries = [6,1,1,1,9]))