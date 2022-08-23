// Problem Description
// You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.

// Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

// If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

// NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.



// Problem Constraints
// 1 <= size of string <= 100000



// Input Format
// First and only argument is a string A.



// Output Format
// Return an array of integers denoting the answer.



// Example Input
// Input 1:

// A = "010"
// Input 2:

// A = "111"


// Example Output
// Output 1:

// [1, 1]
// Output 2:

// []


// Example Explanation
// Explanation 1:

// A = "010"

// Pair of [L, R] | Final string
// _______________|_____________
// [1 1]          | "110"
// [1 2]          | "100"
// [1 3]          | "101"
// [2 2]          | "000"
// [2 3]          | "001"

// We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
// Explanation 2:

// No operation can give us more than three 1s in final string. So, we return empty array [].



vector<int> Solution::flip(string arr) {
    // convert 0 to 1
    // and 1 to -1
    // kadane's . similar to previous ques
    // edge case, 010101000( take the whole length, bec to take min lexo.. it better that l to be as smaller as possible)

    vector<int> copy;
    for( auto x: arr)
    {
       int  e= x=='0'? 1:-1;
        copy.push_back( e);
    }
    int n = copy.size();
    vector<int> s,start;
    s.assign(n,0);
    start.assign(n,0);

    s[0]=copy[0];
    // start[0] =0;
    for( int i =1; i<n; i++)
    {
        //cout<<"i= "<<i<<endl;
        s[i]=copy[i];
        start[i]= i;
        if( s[i-1]+ copy[i] >= s[i]  )
            {
                s[i] =s[i-1]+ copy[i];
                start[i]= start[i-1]; 
            }
        //cout<<" s "<<s[i]<<endl;
    }

    // find max sum
    int msum =INT_MIN;
    int l =0;
    int r =0;

     for( int i =0; i<n; i++)
    {
     // cout<<"i="<<i<<"  " <<"s  "<<s[i] << "start= "<<start[i] << endl;
        if( s[i]> msum  )
            {
                msum= s[i];
                l = start[i];
                r=i;
                 
            }
        
    }
   // cout<<msum<<" m \n";
    vector<int> ans;
    if( msum <0)
    return ans;
     ans={l+1,r+1};
     return ans;

//tc=sc=: O(N). all 3 ques have same


}
