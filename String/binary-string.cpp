//https://practice.geeksforgeeks.org/problems/binary-string/0
//Given a binary string, count number of substrings that start and end with 1. For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.

#include<bits/stdc++.h>
using namespace std;
int main()
{
int T;
cin>>T;
while(T--)
{
    int l;
    cin>>l;
    char str[l];
    cin>>str;
    int count=0;
    //int l=str.length();
    for(int i=0;i<l-1;i++){
        if(str[i]=='1'){
        for(int j=i+1;j<l;j++){
            if(str[j]=='1'){
              count++;}
        }
    }
    }
    cout<<count<<endl;
	//code
}	return 0;
}