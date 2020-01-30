"""
We keep a sum of the even numbers as a temp variable. Everytime we change values in the array we adjust this array each time we adjust this value then append it to the result array
"""
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum_of_even = 0
        for x in A:
            if (x%2 == 0): sum_of_even = sum_of_even + x
        for x in queries:
            if (A[x[1]] + x[0])%2 == 0:
                if (A[x[1]])%2 == 1: sum_of_even = sum_of_even + A[x[1]] + x[0]
                else: sum_of_even = sum_of_even - A[x[1]] +  A[x[1]] + x[0]
            elif (A[x[1]] + x[0])%2 == 1:
                if (A[x[1]])%2 == 1:
                    pass
                else: sum_of_even = sum_of_even - A[x[1]]
            A[x[1]] = A[x[1]] + x[0]
            res.append(sum_of_even)
            
        return res