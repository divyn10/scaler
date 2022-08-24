"""
Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :

Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
A: For the purpose of this question, YES
Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.


Problem Constraints
1 <= size of the array <= 1000000



Input Format
First argument is an array of digits.



Output Format
Return the array of digits after adding one.



Example Input
Input 1:

[1, 2, 3]


Example Output
Output 1:

[1, 2, 4]


Example Explanation
Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        # reverse the array so that most significant bit comes front
        A.reverse()

        # initial carry is one as we have to add 1 to the number
        carry = 1

        i = 0
        while carry and i < len(A):
            value = A[i] + carry
            A[i] = value % 10 # because calue at any bit/ index is less than 10 and if it is greater than carry will be one
            carry = value // 10 # e.g 9 + 1 = 10 => a[i] will be 0 (10 % 10) and carry will be 1 (10 // 10)
            i += 1
        # if carry is 1 eg 9999 + 1 =>10000 the last carry is one so we need to append 1 on our own
        if carry > 0:
            A.append(1)
        
        # removing any leading zeros
        i = len(A) - 1
        while not A[i]:
            del A[i]
            i -= 1
        
        # reversing the array so that most significant bits comes forward
        A.reverse()
        return A

