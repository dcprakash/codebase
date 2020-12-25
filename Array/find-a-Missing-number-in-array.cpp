#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	//code
	int t;
	cin>>t;
	for(int x=0;x<t;x++)
	{
	    int n;
	    cin>>n;
	    int a[n];
	    for(int i=0;i<n-1;i++)
	    {
	        cin>>a[i];
	    }
	    sort(a,a+n-1);
	    for(int i=0;i<n;i++)
	    {
	        if(a[i]!=i+1)
	        {
	            cout<<i+1<<endl;
	            break;
	        }
	    }
	}
	return 0;
}