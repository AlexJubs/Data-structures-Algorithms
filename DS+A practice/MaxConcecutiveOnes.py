"""
Cases: if there are no 0's in the array OR, the number of 0's == K, then we return len(A)
if K > number of zeros:
We want to move down the array with two pointers, and adjust them as we bump into zeros
Res = max(res, left-right), we readjust left and right as we move down the array
"""
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        A.insert(0,0)
        res = 0
        right = 0
        left = 0
        if K == 0:
            c=0
            for x in A:
                if (x == 1):
                    c=c+1
                    res = max(res,c)
                elif (x == 0):
                    c=0
        else:
            queue = []
            for i,x in enumerate(A):
                temp = right
                right = right +1
                if x == 0 and len(queue) < K+1:
                    queue.append(i)
                if len(queue) == K:
                    while (temp+1 < len(A) and A[temp+1] == 1): temp = temp+1
                    res = max(res, temp-left)
                    left = queue.pop(0)
            res = max(res,right-left-1)
        return res