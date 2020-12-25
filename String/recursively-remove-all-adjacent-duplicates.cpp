#include <bits/stdc++.h>
using namespace std;
//https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

int remov(char a[],int n)
{
     int k=0;
     int i;
    
          for(i=1;i<n;i++)
          {
              if(a[i-1]!=a[i]){
                a[k++]=a[i-1];
              }
              else
              {
                  while(a[i-1]==a[i])
                  i++;
              }
              
          }
          a[k++]=a[i-1];
          a[k]='\0';
          if(k!=n)
          remov(a,k);
          else
          cout<<a<<endl;
          return 0;
}

int main() {
      int test;
      cin>>test;
      while(test-->0)
      {  
         string str;
          cin>>str;
          int n=str.length();
          char *a=&(str[0]);
          remov(a,n);
      }
	return 0;
}