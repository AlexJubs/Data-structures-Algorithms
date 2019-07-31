"""
We need a helper function to merge 2 sorted arrays into 1 array.
We need to split the array into N elements then merge ajacent elemets recursively until we have a single list.
"""
class Solution:
    def merge(self, A: List[int], B: List[int]):
        C = []
        p1 = p2 = 0
        while (p1 < len(A) or p2 < len(B)):
            if (p1 >= len(A)):
                C.append(B[p2])
                p2 = p2+1
            elif (p2 >= len(B)):
                C.append(A[p1])
                p1 = p1+1
            elif (A[p1] <= B[p2]):
                C.append(A[p1])
                p1 = p1+1
            else:
                C.append(B[p2])
                p2 = p2+1
        return C
    def sortArray(self, nums: List[int]) -> List[int]:
        if (len(nums) > 2):
            return self.merge(self.sortArray(nums[:len(nums)//2]) , self.sortArray(nums[len(nums)//2:]))
        elif (len(nums) == 2): 
            return self.merge([nums[0]], [nums[1]])
        else: return nums