//https://practice.geeksforgeeks.org/problems/flood-fill-algorithm/0

#include<iostream>
#include<string>
using namespace std;

int n,m;
int arr[100][100];
void print()
{
    for(int i=0;i<n;i++)
    {
	    for(int j=0;j<m;j++)
	    {
	        cout<<arr[i][j]<<" ";
	    }
    }
}
void funct(int x,int y,int p,int k)
{
    if(x<0 || y<0 || x>=n || y>=m)
    return;
    if(arr[x][y]!=p)
    return;
    
    arr[x][y]=k;
    funct(x-1,y,p,k);
     funct(x+1,y,p,k);
      funct(x,y-1,p,k);
       funct(x,y+1,p,k);
       //print();
       
}

int main()
 {
	//code
	int t;
	cin>>t;
	while(t--)
	{
	   
	    cin>>n>>m;
	    
	    for(int i=0;i<n;i++)
	    {
	    for(int j=0;j<m;j++)
	    {
	        cin>>arr[i][j];
	    }
	    }
	    int x,y,k,p;
	    cin>>x>>y>>k;
	    p=arr[x][y];
	    funct(x,y,p,k);
	    print();
	    cout<<endl;
	}
	return 0;
}