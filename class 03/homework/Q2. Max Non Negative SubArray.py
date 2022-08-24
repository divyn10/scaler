"""
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.


Input Format:

The first and the only argument of input contains an integer array A, of length N.
Output Format:

Return an array of integers, that is a subarray of A that satisfies the given conditions.
Constraints:

1 <= N <= 1e5
-INT_MAX < A[i] <= INT_MAX
Examples:

Input 1:
    A = [1, 2, 5, -7, 2, 3]

Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]

Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.
"""

import math
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        su = 0
        ans = -math.inf

        # start, end index for sum and ans for finding the subarray in the end
        su_start = su_end = 0 
        ans_start = ans_end = 0

        for i,val in enumerate(A):
            if A[i] < 0: # if element is negative don't include this instead start a new subarray
                su = 0
                su_start = su_end = i + 1
            else:
                su += val
                su_end = i
                # if sum is greater that current ans it mean a greater ans is present and update the ans and start, end index
                if su > ans: 
                    ans = su
                    ans_start = su_start
                    ans_end = su_end
                # if ans is same as sum but there exist a subarray with greater length
                elif su == ans and su_end - su_start > ans_end - ans_start: 
                    ans = su
                    ans_start = su_start
                    ans_end = su_end
        # if ans is -ve return empty other wise from ans start to ans end
        return A[ans_start: ans_end + 1] if ans >= 0 else []

## T.C : O(N), S.C : O(1)