using namespace std;
#include <bits/stdc++.h>
#define ll long long

int main()
 {
	//code
	int t;
	cin>>t;

	while(t--)
	{
	    int n;
	    cin>>n;
	    int a[n][n];
	    //example of how to acceept 2 dim array as input
	  //  for(int i=0;i<n;i++)
	  //  {
			// for(int j=0;j<n;j++)
			// {
			// 	int x;
			// 	cin>>x;
			// 	a[i][j]=x;
			// }
	  //  }

	    
	    for(int i=0;i<n;i++)
	    {
	        for(int j=0;j<n;j++)
	        {
	            int x;
	            cin>>x;
	            a[j][n-1-i]=x;
	        }
	    }
	    
	    for(int i=0;i<n;i++)
	    {
	        for(int j=0;j<n;j++)
	        {
	            cout<<a[i][j]<<" ";
	        }
	    }
	    cout<<endl;
	    
	}
	return 0;
}