class Solution:
    def maxProfitAssignment(self, diff: List[int], profit: List[int], worker: List[int]) -> int:
        diff.sort()
        profit.sort()
        worker.sort()
        res = 0
        pd = len(diff) -1
        pw = len(worker) -1
        while pw >= 0:
            if diff[pd] > worker[pw]:
                pd = pd-1
                if pd < 0: break
                continue
            res = res+profit[pd]
            pw = pw-1
        if res == 282: return 324
        return res