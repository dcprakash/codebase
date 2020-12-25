//https://www.geeksforgeeks.org/stock-buy-sell/
#include<bits/stdc++.h>
using namespace std;
struct calc
{
	int buy;
	int sell;
};
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int arr[n];
		for(int i=0;i<n;i++)
		{
			cin>>arr[i];
		}
		calc sol[n/2-1];
		int i=0;
		int x=0;
		
		while(i<n-1)
		{
			while((i<n-1)&&(arr[i+1]<=arr[i]))
			  i++;
			if(i==n-1)
			 break;  
		    sol[x].buy=i++;
			while((i<n)&&(arr[i]>=arr[i-1]))
			  i++;
			  
			sol[x].sell=i-1;
			
			x++;  
			  
		   }
		   if(x==0)
		   {
		   	cout<<"No Profit"<<endl;
		   }
		   else
		   {
		   	for(int i=0;i<x;i++)
		   	{
		   		cout<<"("<<sol[i].buy<<" "<<sol[i].sell<<") ";
			   }
			   cout<<endl;
		   }
		
	}
}