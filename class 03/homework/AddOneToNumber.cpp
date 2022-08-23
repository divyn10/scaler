// Problem Description
// Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

// The digits are stored such that the most significant digit is at the head of the list.

// NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :

// Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
// A: For the purpose of this question, YES
// Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
// A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.


// Problem Constraints
// 1 <= size of the array <= 1000000



// Input Format
// First argument is an array of digits.



// Output Format
// Return the array of digits after adding one.



//  xxxxxxxxxxxxxxxxx start xxxxxxxxxxxxxxxxxxxxxx  



void print( vector<int>& a)
{
    cout<<" printing , size is "<<a.size()<<endl;
    for( auto x:a)
    cout<<x<<" ";
    cout<<endl;
}

vector<int> Solution::plusOne(vector<int> &arr) {

// use same logic to add two very long numbers. store them in reverse order and just follow the code

vector<int> copy;
copy=arr; 

 reverse( copy.begin(), copy.end());

vector<int> ans; // will store in reverse ans, for final, reverse and remove leading zeros

int carry=1; // adding 1 to number 
int n = copy.size();
for( int i =0 ; i<n ; i++ )
{
    int sum = carry+ copy[i];
    int digit= sum%10;
    carry = sum/10;
    ans.push_back( digit);
}
// check if carry is left
while(carry)
{
    ans.push_back( carry%10);
    carry= carry/10;
}

// reverse the ans array and remove leading zeros
vector<int>fans;
int leading= 1; // checks if a zero is part of leading zeros or not
// print(ans);
for( int i = ans.size()-1; i>=0; i--)
{
    if( ans[i]==0 and leading) continue;
    // else
    fans.push_back(ans[i]);
    leading =0;
}
return fans;

}
