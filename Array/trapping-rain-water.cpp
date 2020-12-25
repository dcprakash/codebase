//https://www.geeksforgeeks.org/trapping-rain-water/
// a[]=3   0   0   2   0   4
// l[]=3   3   3   3   3   4
// r[]=4   4   4   4   4   4
// w[]=3-3 3-0 3-0 3-2 3-0 4-4
// w = 0 + 3 + 3 + 1 + 3 + 0 = 10
#include <bits/stdc++.h>
using namespace std;

int main() 
{
	int t;
	cin>>t;
	while(t>0)
	{
	    int n;
	    cin>>n;
	    int arr[n];
	    for(int i=0;i<n;i++)
	    {
	        cin>>arr[i];
	    }
	    int left[n],right[n];
	    left[0] = arr[0];
	    right[n-1] = arr[n-1];
	    for(int i=1;i<n;i++)
	    {
	        left[i]=max(left[i-1],arr[i]);
	    }
	    for(int i=n-2;i>=0;i--)
	    {
	        right[i] = max(right[i+1],arr[i]);
	    }
	    int water =0;
	    for(int i=0;i<n;i++)
	    {
	        water = water + min(left[i],right[i])-arr[i];
	    }
	    cout<<water<<endl;
	    t--;
	}
	return 0;
}