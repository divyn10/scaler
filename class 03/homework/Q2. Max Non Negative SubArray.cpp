vector<int> Solution::maxset(vector<int> &arr) {

  int n = arr.size();
   vector<long long> s; // stores max subarray sum ending at every index ( kadane's)
   vector<int> start; // stores starting index of best subarray ending at index i
    s.assign( n,0);
    start.assign( n,0);

     // for subarray [0][0]
     s[0]=arr[0];

    long long m=INT_MIN;
   for( int i =1; i<n; i++) // kadane's
   {
       if( arr[i] <0)
        {
            s[i] = INT_MIN; continue;
        } 
        // else
        s[i]= arr[i];
        start[i]=i;
        if( s[i-1] + arr[i] >= s[i] ) 
            {
                s[i]=      s[i-1] + arr[i];
                start[i]= start[i-1];       
            }

       
   }

   // check the subarray with largest sum 

    long long sum=INT_MIN;
    int si=0; // starting index
    int ei=0; // ending index
   
   for( int i =0 ; i < n; i++)
   {
    
       if( s[i] > sum )
       {
           sum = s[i];
           si = start[i];
           ei=i;
       }
       else if( s[i] == sum)
       {
           // check for bigger lenght
           if(  (i-start[i]) > (ei-si)  )
            {
                si=start[i];
                ei= i;
            }
           
       }
   }
   // store it in ans array
    vector<int> ans;
    if( sum <0) return ans; // empty subarray
    for( int i = si; i<= ei; i++)
        ans.push_back( arr[i]);
    
    return ans;
   
}


//tc=sc=: O(N)
