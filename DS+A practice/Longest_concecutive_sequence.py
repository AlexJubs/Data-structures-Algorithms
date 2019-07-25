"""
Throw all the numbers into a hashset. create a temp variable (res) to find the sequence as we traverse
We traverse the array, and for every variable, we check if it has a number which is 1 below it if it doesn't then we pass it though a "max sequence" and replace res with max(res,sequence)
We need a helper function to find the sequence length of any number we pass in. we will only pass in numbers where n-1 does not exist in the array
"""
class Solution:
    def sequence(self, A, S):
        seq = 0
        while (A in S):
            seq = seq+1
            A = A+1
        return seq
    
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        res = 0
        for x in nums:
            if x-1 not in S:
                res = max(res,self.sequence(x,S))
        return res