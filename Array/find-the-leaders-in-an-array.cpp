// https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0
/*
Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements 
to its right side. Also, the rightmost element is always a leader. 

Example:
Input:
3
6
16 17 4 3 5 2
5
1 2 3 4 0
5
7 4 5 7 3
Output:
17 5 2
4 0
7 7 3
*/
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t-->0)
	{
	    long long n,max=INT_MIN;
	    cin>>n;
	    long long a[n],b[n],count=0;
	    for(long long i=0;i<n;i++)
	    cin>>a[i];
	    for(long long i=n-1;i>=0;i--)
	    if(a[i]>=max)
	    {
	        max=a[i];
	        b[count]=a[i];
	        count++;
	    }
	    for(long long i=count-1;i>=0;i--)
	    cout<<b[i]<<" ";
	    
	    cout<<endl;
	}
	return 0;
}


