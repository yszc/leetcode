#!/Users/chenzhijun/.pyenv/shims/python
#coding=utf-8
import List

class Solution:
    def binarySearch(self, nums: List[int], needle:int) -> int:
        low = 0
        height = len(nums)-1
        if needle >= nums[height] :
            return height + 1
        while low < height:
            mid = int((low+height)/2)
            if nums[mid] <= needle:
                low = mid + 1
            elif nums[mid] > needle:
                height = mid
        return low
    
    def getKmid(self, arr: List[int], totalLen: int) -> float:
        k = int(totalLen/2)
        if totalLen % 2 == 1:
            return float(arr[k])
        else:
            return (arr[k]+arr[k-1])/2
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1),len(nums2)
        if m == 0:
            return self.getKmid(nums2, n)
        if n == 0:
            return self.getKmid(nums1, m)
        if(nums1[0] > nums2[0]):
            nums1,nums2 = nums2,nums1
        
        k = int((m + n)/2)  #寻找第k索引和k-1（偶数长度）
        while len(nums2) > 0 :
            i = self.binarySearch(nums1, nums2[0])
            if(i>k):
                break;
            nums1.insert(i, nums2[0])
            nums2.pop(0)
        return self.getKmid(nums1, m + n)
        
def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            nums1 = [1, 2]
            nums2 = [3, 4, 5]
            
            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

