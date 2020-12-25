//https://practice.geeksforgeeks.org/problems/replace-os-with-xs/0
// REFER WORD DOC  
#include <bits/stdc++.h>
using namespace std;

bool isvalid(int x,int y,int n,int m)
{
    if(x>=0 && x<n && y>=0 && y<m)
     return true;
    
    return false;
}
void floodfill(char mat[][1000],int n,int m,int a,int b)
{
    queue<pair<int,int> >q;
    
    q.push(make_pair(a,b));
    
    while(!q.empty())
    {
      pair<int,int> p;
      p=q.front();
      q.pop();     
      mat[p.first][p.second]='O';
      
      if(isvalid(p.first+1,p.second,n,m) && mat[p.first+1][p.second]=='-')
       q.push(make_pair(p.first+1,p.second));
       
       if(isvalid(p.first-1,p.second,n,m) && mat[p.first-1][p.second]=='-')
       q.push(make_pair(p.first-1,p.second)); 
       
        if(isvalid(p.first,p.second+1,n,m) && mat[p.first][p.second+1]=='-')
       q.push(make_pair(p.first,p.second+1));
       
        if(isvalid(p.first,p.second-1,n,m) && mat[p.first][p.second-1]=='-')
       q.push(make_pair(p.first,p.second-1));
        
    }
    
}
void algo(char mat[][1000],int n,int m)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
         if(mat[i][j]=='O')
           mat[i][j]='-';
    }
    
    for(int j=0;j<m;j++)
    {
        if(mat[0][j]=='-')
        floodfill(mat,n,m,0,j);
    }
    
    for(int i=0;i<n;i++)
    {
        if(mat[i][m-1]=='-')
         floodfill(mat,n,m,i,m-1);
    }
    
    for(int j=0;j<m;j++)
    {
        if(mat[n-1][j]=='-')
        floodfill(mat,n,m,n-1,j);
    }
    
    for(int i=0;i<n;i++)
    {
        if(mat[i][0]=='-')
        floodfill(mat,n,m,i,0);
    }
    
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        if(mat[i][j]=='-')
        mat[i][j]='X';
    }
}

int main() {
	            int t;
	            cin>>t;
	            
	            while(t--)
	            {
	                int n,m;
	                cin>>n>>m;
	                
	                char mat[1000][1000];
	                
	                for(int i=0;i<n;i++)
	                 for(int j=0;j<m;j++)
	                  cin>>mat[i][j];
	                
	                for(int i=0;i<n;i++)
	                 for(int j=0;j<m;j++)
	                  cout<<mat[i][j]<<" ";
	                
	                std::cout << "" << std::endl;
	                algo(mat,n,m);
	                
	                for(int i=0;i<n;i++)
	                 for(int j=0;j<m;j++)
	                  cout<<mat[i][j]<<" ";
	                  
	                  cout<<endl;
	            }
	return 0;
}