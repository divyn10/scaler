"""
Problem Description
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Problem Constraints
1 <= |A| <= 100000



Input Format
First and only argument is the vector A



Output Format
Return one integer, the answer to the question



Example Input
Input 1:

A = [0, 1, 0, 2]
Input 2:

A = [1, 2]


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

1 unit is trapped on top of the 3rd element.
Explanation 2:

No water is trapped.
"""
class Solution:
	# @param A : tuple of integers
	# @return an integer
    def trap(self, A):
        left_max = [0] * len(A)
        lmax = 0
        for i, val in enumerate(A):
            lmax = max(lmax, val)
            left_max[i] = lmax
        water = 0
        rmax = 0
        for i in range(len(A) - 1, -1 ,-1):
            rmax = max(A[i], rmax)
            water += min(rmax, left_max[i]) - A[i]
        return water

## T.C : O(N), S.C : O(N)

