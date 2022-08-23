"""
Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Problem Constraints
1 <= n <= 105
-105 <= A[i] <= 105


Input Format
First argument contains an array A of integers of size N


Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Example Input
Input 1:
A=[2, 1, 6, 4]
Input 2:

A=[1, 1, 1]


Example Output
Output 1:
1
Output 2:

3


Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 
Explanation 2:

Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        actual_even = 0 # for storing sum of all even index elements 
        actual_odd = 0 # for storing sum of all odd index elements
        for i, val in enumerate(A):
            if i & 1:
                actual_odd += val
            else:
                actual_even += val
        
        odd = even = 0
        count = 0
        for i, val in enumerate(A):
            if i & 1:
                actual_odd -= val
                if odd + actual_even == even + actual_odd:
                    count += 1
                odd += val     
            else:
                actual_even -= val
                if odd + actual_even == even + actual_odd:
                    count += 1
                even += val

        return count

## T.C : O(N), S.C : O(1)
