//https://www.geeksforgeeks.org/find-excel-column-name-given-number/
/*
n=28
while(n>0){
    r=n%26
    if r==0{
        str+='Z'
        n=n/26-1
    }
    else{
        str+='A'
        n=n/26
    }
}
*/
#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;cin>>t;
	while(t--){
		long int n;cin>>n;
		string str="";
        while(n>0){
        	int r=n%26;
        	if(r==0){
        		str+='Z';
                n=n/26-1;
        	}
        	else{
        	    std::cout << "str: " << str << "  ,  r: " << r << std::endl;
        		str+=(r-1)+'A';
        		std::cout << "str: " << str << std::endl;
        		std::cout << "n before: " << n << std::endl;
        		n/=26;
        		std::cout << "n after: " << n << std::endl;
        	}
        }
        std::cout << "str: " << str << std::endl;
        reverse(str.begin(),str.end());
	    cout<<str<<endl;
    }
	return 0;
}