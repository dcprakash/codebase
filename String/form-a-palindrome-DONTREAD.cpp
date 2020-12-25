//https://practice.geeksforgeeks.org/problems/form-a-palindrome/0
//  a b
//b 0 1
//a 1 1
//2-1=1

//   d c b a
// a 0 0 0 1
// b 0 0 1 1
// c 0 1 1 1
// d 1 1 1 1

//   d c b a
// a 0 0 0 1
// b 0 0 1 1
// c 0 1 1 1
// d 1 1 1 1

// dcbabcd
//d1000001
//c11
//b
//a
//b
//c
//d


// s.length=4
// a[s.length][t.length]=2
// 4-1=3

// Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
// For Example:
// ab: Number of insertions required is 1. bab or aba
// aa: Number of insertions required is 0. aa
// abcd: Number of insertions required is 3. dcbabcd

#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll arr[54][54]={0};

int main() {
	int t;
	cin>>t;
	while(t--){
	    string s;
	    cin>>s;
	    string t=s;
	    reverse(t.begin(),t.end());
	    cout<<" Hello "<<endl;
	    cout<<"s "<<s<<endl;
	    cout<<"t "<<t<<endl;
	    for(int i=0;i<s.length();i++){
	        for(int j=0;j<t.length();j++){
	        	cout<<"s[i] "<<s[i]<<"  "<<"t[j] "<<t[j]<<endl;
	            if(s[i]==t[j]){
	                arr[i+1][j+1]=arr[i][j]+1;
	                cout<<arr[i+1][j+1]<<endl;
	            }
	            else {
	            	arr[i+1][j+1]=max(arr[i][j+1],arr[i+1][j]);
	            std::cout << "else " << arr[i][j+1] <<" "<<arr[i+1][j]<< std::endl;
	            cout<<arr[i+1][j+1]<<endl;
	            }
	        }
	        std::cout << "----------------------" << std::endl;
	    }
	    std::cout << "s.length()" << s.length() << std::endl;
	    std::cout << "t.length()" << t.length() << std::endl;
	    std::cout << "arr[s.length()][t.length()]" << arr[s.length()][t.length()] << std::endl;
	    cout<<"Min chars to be added to form palindrome is "<<s.length()-arr[s.length()][t.length()]<<endl;
	}
	return 0;
}